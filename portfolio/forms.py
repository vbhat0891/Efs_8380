from django import forms
from .models import Customer, Investment, Stock, Fund


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = (
            'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)


class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ('customer', 'symbol', 'name', 'quantity', 'purchase_price', 'purchase_date',)
