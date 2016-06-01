# Product Book API
```sh
[GET] URI::products/
```
This url will return a list of products

```sh
[
    {
        "id": 1,
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    },
    {
        "id": 3,
        "name": "Product2",
        "price": 80.0,
        "stock": 2000.0,
        "unit": "KG"
    }
]
```



```sh
[POST] URI::products/
```

This url will use to save a product. It will return 201 for success and 404 for fail. The product payload JSON will be like this.

    {
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    }

returned product JSON will be like this


    {
        "id": 4,
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    }

```sh
[GET] URI::products/product_id/
```

This url will use to view a particular product detail. It will return 200 for success and 404 for product not found. The product JSON will be like this.

    {
    	"id": 4,
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    }

```sh
[PUT] URI::products/product_id/
```

This url will use to update a particular product detail. It will return 201 for success and 404 for product not found. The product payload JSON will be like this.

	{
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    }

returned product JSON will be like this


    {
        "id": 4,
        "name": "Product1",
        "price": 10.0,
        "stock": 5000.0,
        "unit": "KG"
    }

 ```sh
[DELETE] URI::products/product_id/
```

This url will use to delete a particular product detail. It will return 204 for success and 404 for product not found.

```sh
[DELETE] URI::products/?p=product_name
```

This url will use to search products by their name. It will return product object array for match otherwise will return empty array
