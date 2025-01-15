# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Ticket(models.Model):
    _name = "cesta.ticket"
    _description = "Ticket de Compra"

    fecha = fields.Datetime(string="Fecha de Emisión", default=fields.Datetime.now, required=True)
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    cliente_id = fields.Many2one('cesta.cliente', string="Cliente", required=True)
    linea_ticket_ids = fields.One2many('cesta.linea_ticket', 'ticket_id', string="Líneas del Ticket")

    @api.depends('linea_ticket_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(linea.subtotal for linea in record.linea_ticket_ids)


class Ticket(models.Model):
    _name = "cesta.ticket"
    _description = "Ticket de Compra"

    fecha = fields.Datetime(string="Fecha de Emisión", default=fields.Datetime.now, required=True)
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    cliente_id = fields.Many2one('cesta.cliente', string="Cliente", required=True)
    linea_ticket_ids = fields.One2many('cesta.linea_ticket', 'ticket_id', string="Líneas del Ticket")

    @api.depends('linea_ticket_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(linea.subtotal for linea in record.linea_ticket_ids)

    @api.model
    def create(self, vals):
        # Crear el ticket
        ticket = super(Ticket, self).create(vals)
        cliente = ticket.cliente_id

        # Validar saldo suficiente
        if cliente.saldo_monedero < ticket.total:
            raise ValueError(f"El cliente {cliente.nombre} no tiene suficiente saldo en el monedero para esta compra.")

        # Descontar del monedero del cliente
        cliente.saldo_monedero -= ticket.total
        cliente.saldo_monedero = round(cliente.saldo_monedero, 2)  # Redondear para evitar errores de coma flotante
        return ticket

    def write(self, vals):
        for record in self:
            # Actualizar las líneas del ticket si cambian
            if 'linea_ticket_ids' in vals or 'cliente_id' in vals:
                cliente = record.cliente_id
                nuevo_total = sum(linea.subtotal for linea in record.linea_ticket_ids)

                # Verificar que el cliente tiene suficiente saldo
                if cliente.saldo_monedero < nuevo_total:
                    raise ValueError(f"El cliente {cliente.nombre} no tiene suficiente saldo en el monedero para esta compra.")

                # Actualizar el saldo del cliente
                cliente.saldo_monedero -= nuevo_total - record.total
                cliente.saldo_monedero = round(cliente.saldo_monedero, 2)

        return super(Ticket, self).write(vals)



class LineaTicket(models.Model):
    _name = "cesta.linea_ticket"
    _description = "Línea de Ticket"

    ticket_id = fields.Many2one('cesta.ticket', string="Ticket", required=True)
    producto_id = fields.Many2one('cesta.producto', string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)
    precio_unitario = fields.Float(string="Precio Unitario", related='producto_id.precio', readonly=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario

    @api.model
    def create(self, vals):
        # Buscar el producto y descontar el stock
        producto = self.env['cesta.producto'].browse(vals['producto_id'])
        if producto.stock < vals['cantidad']:
            raise ValueError(f"El producto {producto.nombre} no tiene suficiente stock.")
        producto.stock -= vals['cantidad']
        return super(LineaTicket, self).create(vals)

    def write(self, vals):
        for record in self:
            if 'cantidad' in vals:
                cantidad_nueva = vals['cantidad']
                diferencia = cantidad_nueva - record.cantidad

                if record.producto_id.stock < diferencia:
                    raise ValueError(
                        f"El producto {record.producto_id.nombre} no tiene suficiente stock para aumentar la cantidad.")

                record.producto_id.stock -= diferencia

        return super(LineaTicket, self).write(vals)

    def unlink(self):
        # Revertir el stock al eliminar una línea de ticket
        for record in self:
            record.producto_id.stock += record.cantidad
        return super(LineaTicket, self).unlink()

    ticket_name = fields.Char(string="Ticket", compute="_compute_ticket_name", store=True)

    @api.depends('ticket_id', 'ticket_id.cliente_id')
    def _compute_ticket_name(self):
        for record in self:
            record.ticket_name = f"Ticket de {record.ticket_id.cliente_id.nombre}" if record.ticket_id else "Sin Ticket"


class Producto(models.Model):
    _name = "cesta.producto"
    _description = "Producto"

    nombre = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", default=0, required=True)
    categoria_id = fields.Many2one('cesta.categoria_producto', string="Categoría")


class CategoriaProducto(models.Model):
    _name = "cesta.categoria_producto"
    _description = "Categoría de Producto"

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    producto_ids = fields.One2many('cesta.producto', 'categoria_id', string="Productos")


class CestaCliente(models.Model):
    _name = 'cesta.cliente'
    _description = 'Cliente de Cesta de Compra'

    nombre = fields.Char(string="Nombre")
    email = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")
    saldo_monedero = fields.Float(string="Saldo en Monedero")
    ticket_ids = fields.One2many('cesta.ticket', 'cliente_id', string="Tickets")
    country_id = fields.Many2one('res.country', string="País")  # Relación con res_country

