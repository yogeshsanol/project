from celery import shared_task
from app.models.product import Product
from app.models.category import Category


@shared_task
def generate_product_task(number):
    try:
        for i in range(1,number):
            print(f"Product {i} generated")
            title = f"Product {i}"
            description = f"Description for product {i}"
            price = i * 10.0
            category_id = Category.objects.get(id=1)
            status = "ACTIVE"
            Product.objects.create(title=title, description=description, price=price,category_id=category_id,status=status)
        return f"{number} products generated successfully"
    except Exception as e:
        print(f"Error generating products: {e}")
        return f"Error generating products: {e}"    