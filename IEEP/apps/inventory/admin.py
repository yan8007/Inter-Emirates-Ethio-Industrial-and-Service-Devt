from django.contrib import admin
from .models import Warehouse, StockItem, StockTransaction, ReorderAlert, Order, OrderItem

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'code']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'warehouse', 'quantity', 'batch_number', 'procurement_status', 'expiry_date', 'created_at']
    list_filter = ['warehouse', 'procurement_status', 'expiry_date', 'created_at']
    search_fields = ['product__sku', 'product__name', 'batch_number', 'location', 'notes']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('product', 'warehouse', 'quantity', 'unit_cost', 'batch_number', 'location')
        }),
        ('Status and Dates', {
            'fields': ('procurement_status', 'expiry_date', 'manufactured_date', 'reorder_threshold')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
