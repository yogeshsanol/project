1. Install Required Python Packages using below command : 
pip install -r requirement.txt

2. Run Django Project using below command :
python manage.py runserver


3. Curls of APIs 

    3.1 Obtain Auth Token using Username and password
        curl --location 'http://127.0.0.1:8000/api-token-auth/' \
        --header 'Content-Type: application/json' \
        --data '{
            "username": "yogesh",
            "password": "12345qwerty"
        }'

    3.2. Get Product : 
        curl --location 'http://127.0.0.1:8000/app/product/' \
        --header 'Authorization: Token 381126111405c39acbe9572b856f158e453c9e1c'

    3.3. POST  Create Product   
        curl --location 'http://127.0.0.1:8000/app/product/' \
        --header 'Authorization: Token 381126111405c39acbe9572b856f158e453c9e1c' \
        --header 'Content-Type: application/json' \
        --data '{
                "title": "Product 2",
                "description": "Test Description",
                "price": "20.00",
                "status": "ACTIVE",
                "category_id": 1
            }'

    3.4. POST Create Category
        curl --location 'http://127.0.0.1:8000/app/category/' \
        --header 'Authorization: Token 381126111405c39acbe9572b856f158e453c9e1c' \
        --header 'Content-Type: application/json' \
        --data '{
                "name": "Food"
            }'  

    3.5. POST Generate Dummy Products
        curl --location 'http://127.0.0.1:8000/app/generate-product/' \
        --header 'Authorization: Token 381126111405c39acbe9572b856f158e453c9e1c' \
        --header 'Content-Type: application/json' \
        --data '{"number":50}'

    3.6 POST Download/Export CSV File of Product data
        curl --location --request POST 'http://127.0.0.1:8000/app/download-product/' \
        --header 'Authorization: Token 381126111405c39acbe9572b856f158e453c9e1c'    





