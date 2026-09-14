# Creating a Receipt with Subtotal, VAT, and Total Amount

from pyscript import display, document

def create_order(e):
        prod1 = document.getElementById("drink1")
        prod2 = document.getElementById("drink2")
        prod3 = document.getElementById("drink3")

        subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked 
        display(f'The subtotal is {subtotal}', target="result")

        vat_number = subtotal * 0.12 
        display(f'The VAT is {vat_number}', target="result")

        total_amount = subtotal + vat_number 
        display(f'The total amount is {total_amount}', target="result")