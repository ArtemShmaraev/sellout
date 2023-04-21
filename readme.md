<a name="up"></a>

# SellOut API

Небольшое пояснение: первые квадратные скобки перед запросом это тип запроса, вторые это уровень доступа  (Admin >User >
Anon)

## User API

1. `[GET][Admin] user` информация обо всех пользователях, списком [Вниз к запросу](#users)
2. `[GET][Admin] user/<user_id>` данные пользователя [Вниз к запросу](#user_id)
3. `[GET][User] user_info/<user_id>` данные пользователя [Вниз к запросу](#user_id)
4. `[POST][Anon] user/register` регистрация пользователя [Вниз к запросу](#reg)
5. `[POST][Anon] user/login` вход в систему [Вниз к запросу](#log)
6. `[GET][User] user/last_seen/<user_id>` последние 7 просмотренных товаров пользователя [Вниз к запросу](#last)

## Product API

1. `[GET][Admin] product` все товары [Вниз к запросу](#products)
2. `[GET][Admin] product/<product_id>` данные одного товара [Вниз к запросу](#product_id)
3. `[GET][Anon] product/all/<num_page>` страница товаров [Вниз к запросу](#product_all)

## Shipping API

1. `[GET][Anon] product_unit/product/<product_id>` все product_unit для данного товара [Вниз к запросу](#product_unit)
2. `[GET][Anon] product_unit/product_main/<product_id>/<user_id>` "картока товара" [Вниз к запросу](#product_main)

## WishList API

1. `[GET][User] wishlist/<user_id>` вишлист пользователя [Вниз к запросу](#wl)
2. `[POST][User] wishlist/add/<user_id>/<product_id>/<size_id>` добавление в вишлист [Вниз к запросу](#add_wl)
3. `[DELETE][User] wishlist/delete/<wishlist_unit_id>` Удаление из вишлиста [Вниз к запросу](#del_wl)
4. `[POST][User] wishlist/add_no_size/<user_id>/<product_id>` добавить товара "без
   размера" [Вниз к запросу](#add_no_size_wl)
5. `[POST][User] wishlist/change_size/<user_id>/<wishlist_unit_id>/<size_id>` поменять размер в
   вишлисте [Вниз к запросу](#change_wl)

## Orders API

1. `[GET][User] order/cart/<user_id>` корзина пользователя [Вниз к запросу](#cart)
2. `[POST][User]  order/cart_add/<user_id>/<product_unit_id>` добавить юнит в корзину [Вниз к запросу](#add_to_cart)
3. `[DELETE][User] cart/cart_delete/<user_id>/<product_unit_id>` удалить юнит из
   корзины [Вниз к запросу](#del_from_cart)
4. `[POST][User] cart/checkout/<user_id>` оформить заказ [Вниз к запросу](#checkout)
5. `[GET][Admin] order/orders` все заказы [Вниз к запросу](#orderss)
6. `[GET][User] order/user_orders` все заказы пользователя [Вниз к запросу](#user_orders)
7. `[GET][User] order/<order_id>` информация о заказе [Вниз к запросу](#order)
   <a name="user"></a>

## User API

[:arrow_up:SellOut API](#up)
<a name="users"></a>

### 1. `[GET][Admin] user` информация обо всех пользователях, списком

Response:

```json
[
  {
    "id": 2,
    "last_login": "2023-04-12T10:07:07Z",
    "is_superuser": false,
    "username": "noadmin",
    "first_name": "no",
    "last_name": "admin",
    "email": "noadmin@mail.ru",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2023-04-12T10:07:34Z",
    "all_purchase_amount": 0,
    "personal_discount_percentage": 0,
    "referral_link": null,
    "preferred_size_grid": null,
    "gender": null,
    "ref_user": null,
    "groups": [],
    "user_permissions": [],
    "my_groups": [],
    "address": [],
    "last_viewed_products": [
      {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      }
    ]
  }
]
```

[:arrow_up:User API](#user)
[:arrow_up:SellOut API](#up)
<a name="user_id"></a>

### 2. `[GET][Admin] user/<user_id>` данные пользователя

Response:

```json
{
  "id": 2,
  "last_login": "2023-04-12T10:07:07Z",
  "is_superuser": false,
  "username": "noadmin",
  "first_name": "no",
  "last_name": "admin",
  "email": "noadmin@mail.ru",
  "is_staff": false,
  "is_active": true,
  "date_joined": "2023-04-12T10:07:34Z",
  "all_purchase_amount": 0,
  "personal_discount_percentage": 0,
  "referral_link": null,
  "preferred_size_grid": null,
  "gender": null,
  "ref_user": null,
  "groups": [],
  "user_permissions": [],
  "my_groups": [],
  "address": [],
  "last_viewed_products": [
    {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": 1,
      "brands": [
        1
      ],
      "categories": [
        1
      ],
      "tags": [
        1
      ]
    },
    {
      "id": 2,
      "name": "Dunk",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "sku",
      "available_flag": true,
      "last_upd": "2023-04-07T15:59:39Z",
      "add_date": "2023-04-07",
      "fit": 0,
      "rel_num": 0,
      "gender": 1,
      "brands": [
        1
      ],
      "categories": [
        1
      ],
      "tags": [
        1
      ]
    }
  ]
}
```

[:arrow_up:User API](#user)
[:arrow_up:SellOut API](#up)
<a name="reg"></a>

### 3. `[POST][Anon] user/register` регистрация пользователя

Body:

```json
{
  "username": "mail@mail.ru",
  "password": "пароль",
  "first_name": "Имя",
  "last_name": "Фамилия",
  "gender": "male"
}

```

Response:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4MjEyOSwiaWF0IjoxNjgxNDc3MzI5LCJqdGkiOiI2ZGExNTQ5MmMyODk0YzVmODhiNWRkN2EyNTcwNTg0MiIsInVzZXJfaWQiOjE3fQ.HhBV5bNIFtEaRaS96q_DAPAu5cdQhfRRHTcSHAl_Ffk",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTYzNzI5LCJpYXQiOjE2ODE0NzczMjksImp0aSI6IjJjY2ZiZjNiZTJhYzQ3YTQ4NWRkNTY4ZGQzNWFiNzRhIiwidXNlcl9pZCI6MTd9.l-PcMX4WeUWmD5-egu1PNlgH_EdQb3tm2uIWUp57MzE"
}
```

[:arrow_up:User API](#user)
[:arrow_up:SellOut API](#up)
<a name="log"></a>

### 4. `[POST][Anon] user/login` вход в систему

Body:

```json
{
  "username": "mail@mail.ru",
  "password": "пароль"
}
```

Response:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4MjEyOSwiaWF0IjoxNjgxNDc3MzI5LCJqdGkiOiI2ZGExNTQ5MmMyODk0YzVmODhiNWRkN2EyNTcwNTg0MiIsInVzZXJfaWQiOjE3fQ.HhBV5bNIFtEaRaS96q_DAPAu5cdQhfRRHTcSHAl_Ffk",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTYzNzI5LCJpYXQiOjE2ODE0NzczMjksImp0aSI6IjJjY2ZiZjNiZTJhYzQ3YTQ4NWRkNTY4ZGQzNWFiNzRhIiwidXNlcl9pZCI6MTd9.l-PcMX4WeUWmD5-egu1PNlgH_EdQb3tm2uIWUp57MzE"
}
```

[:arrow_up:User API](#user)
[:arrow_up:SellOut API](#up)
<a name="last"></a>

### 5. `[GET][User] user/last_seen/<user_id>` последние 7 просмотренных товаров пользователя

Response:

```json
[
  {
    "id": 1,
    "name": "Air Force 1",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "air_force_1",
    "available_flag": true,
    "last_upd": "2023-04-07T15:28:17Z",
    "add_date": "2023-04-07",
    "fit": 1,
    "rel_num": 1,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ],
    "min_price": 7,
    "in_wishlist": true
  },
  {
    "id": 2,
    "name": "Dunk",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "sku",
    "available_flag": true,
    "last_upd": "2023-04-07T15:59:39Z",
    "add_date": "2023-04-07",
    "fit": 0,
    "rel_num": 0,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ],
    "min_price": 100,
    "in_wishlist": false
  }
]
```

[:arrow_up:User API](#user)
[:arrow_up:SellOut API](#up)

<a name="product"></a>

## Product APi

[:arrow_up:SellOut API](#up)
<a name="products"></a>

### 1. `[GET][Admin] product` все товары

Response:

```json
[
  {
    "id": 1,
    "name": "Air Force 1",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "air_force_1",
    "available_flag": true,
    "last_upd": "2023-04-07T15:28:17Z",
    "add_date": "2023-04-07",
    "fit": 1,
    "rel_num": 1,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ]
  },
  {
    "id": 2,
    "name": "Dunk",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "sku",
    "available_flag": true,
    "last_upd": "2023-04-07T15:59:39Z",
    "add_date": "2023-04-07",
    "fit": 0,
    "rel_num": 0,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ]
  }
]
```

[:arrow_up:Product API](#product)
[:arrow_up:SellOut API](#up)
<a name="product_id"></a>

### 2. `[GET][Admin] product/<product_id>` данные одного товара

Response:

```json
{
  "id": 1,
  "name": "Air Force 1",
  "bucket_link": "/buck",
  "description": "desc",
  "sku": "air_force_1",
  "available_flag": true,
  "last_upd": "2023-04-07T15:28:17Z",
  "add_date": "2023-04-07",
  "fit": 1,
  "rel_num": 1,
  "gender": {
    "id": 1,
    "name": "M"
  },
  "brands": [
    {
      "id": 1,
      "name": "Nike"
    }
  ],
  "categories": [
    {
      "id": 1,
      "name": "Sport"
    }
  ],
  "tags": [
    {
      "id": 1,
      "name": "Style"
    }
  ]
}
```

[:arrow_up:Product API](#product)
[:arrow_up:SellOut API](#up)
<a name="product_all"></a>

### 3. `[GET][Anon] product/all/<num_page>` страница товаров

Response:

```json
{
  "page number": 1,
  "items": [
    {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": {
        "id": 1,
        "name": "M"
      },
      "brands": [
        {
          "id": 1,
          "name": "Nike"
        }
      ],
      "categories": [
        {
          "id": 1,
          "name": "Sport"
        }
      ],
      "tags": [
        {
          "id": 1,
          "name": "Style"
        }
      ],
      "min_price": 7,
      "in_wishlist": true
    },
    {
      "id": 2,
      "name": "Dunk",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "sku",
      "available_flag": true,
      "last_upd": "2023-04-07T15:59:39Z",
      "add_date": "2023-04-07",
      "fit": 0,
      "rel_num": 0,
      "gender": {
        "id": 1,
        "name": "M"
      },
      "brands": [
        {
          "id": 1,
          "name": "Nike"
        }
      ],
      "categories": [
        {
          "id": 1,
          "name": "Sport"
        }
      ],
      "tags": [
        {
          "id": 1,
          "name": "Style"
        }
      ],
      "min_price": 100,
      "in_wishlist": false
    }
  ]
}
```

[:arrow_up:Product API](#product)
[:arrow_up:SellOut API](#up)
<a name="shipping"></a>
[:arrow_up:SellOut API](#up)

## Shipping API

<a name="product_unit"></a>

### 1. `[GET][Anon] product_unit/product/<product_id>` все product_unit для данного товара

Response:

```json
[
  {
    "id": 1,
    "final_price": 7,
    "availability": true,
    "product": {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": {
        "id": 1,
        "name": "M"
      },
      "brands": [
        {
          "id": 1,
          "name": "Nike"
        }
      ],
      "categories": [
        {
          "id": 1,
          "name": "Sport"
        }
      ],
      "tags": [
        {
          "id": 1,
          "name": "Style"
        }
      ]
    },
    "size": {
      "id": 1,
      "INT": "12",
      "US": "12",
      "UK": "12",
      "EU": "12",
      "IT": "12",
      "RU": "12",
      "product": {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      }
    },
    "currency": {
      "id": 2,
      "name": "pending"
    },
    "delivery_type": {
      "id": 1,
      "name": "Самолёт"
    },
    "platform": {
      "id": 1,
      "platform": "Poizon",
      "site": "/poizon"
    }
  }
]
```

[:arrow_up:Shipping API](#shipping)
[:arrow_up:SellOut API](#up)
<a name="product_main"></a>

### 2. `[GET][Anon] product_unit/product_main/<product_id>/<user_id>` "картока товара" (если пользователь не авторизован user_id = 0)

Response:

```json
{
  "id": 1,
  "name": "Air Force 1",
  "bucket_link": "/buck",
  "description": "desc",
  "sku": "air_force_1",
  "available_flag": true,
  "last_upd": "2023-04-07T15:28:17Z",
  "add_date": "2023-04-07",
  "fit": 1,
  "rel_num": 1,
  "gender": {
    "id": 1,
    "name": "M"
  },
  "brands": [
    {
      "id": 1,
      "name": "Nike"
    }
  ],
  "categories": [
    {
      "id": 1,
      "name": "Sport"
    }
  ],
  "tags": [
    {
      "id": 1,
      "name": "Style"
    }
  ],
  "min_price": 7,
  "in_wishlist": true
}

```

[:arrow_up:Shipping API](#shipping)
[:arrow_up:SellOut API](#up)

<a name="wishlist"></a>

## WishList API

[:arrow_up:SellOut API](#up)
<a name="wl"></a>

### 1. `[GET][User] wishlist/<user_id>` вишлист пользователя

Response:

```json
[
  {
    "id": 4,
    "product": {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": {
        "id": 1,
        "name": "M"
      },
      "brands": [
        {
          "id": 1,
          "name": "Nike"
        }
      ],
      "categories": [
        {
          "id": 1,
          "name": "Sport"
        }
      ],
      "tags": [
        {
          "id": 1,
          "name": "Style"
        }
      ],
      "min_price": 7,
      "in_wishlist": true
    },
    "size": {
      "id": 2,
      "INT": "0",
      "US": "0",
      "UK": "0",
      "EU": "0",
      "IT": "0",
      "RU": "0",
      "product": 1
    },
    "product_unit": {
      "id": 1,
      "final_price": 7,
      "availability": true,
      "product": {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": {
          "id": 1,
          "name": "M"
        },
        "brands": [
          {
            "id": 1,
            "name": "Nike"
          }
        ],
        "categories": [
          {
            "id": 1,
            "name": "Sport"
          }
        ],
        "tags": [
          {
            "id": 1,
            "name": "Style"
          }
        ]
      },
      "size": {
        "id": 1,
        "INT": "12",
        "US": "12",
        "UK": "12",
        "EU": "12",
        "IT": "12",
        "RU": "12",
        "product": {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        }
      },
      "currency": {
        "id": 2,
        "name": "pending"
      },
      "delivery_type": {
        "id": 1,
        "name": "Самолёт"
      },
      "platform": {
        "id": 1,
        "platform": "Poizon",
        "site": "/poizon"
      }
    }
  }
]
```

[:arrow_up:WishList API](#wishlist)
[:arrow_up:SellOut API](#up)
<a name="add_wl"></a>

### 2. `[POST][User] wishlist/add/<user_id>/<product_id>/<size_id>` добавление в вишлист

Response: карточку вишлиста
<a name="del_wl"></a>

### 3. `[delete][User] wishlist/delete/<wishlist_unit_id>` Удаление из вишлиста

Response: карточку вишлиста
<a name="add_no_size_wl"></a>

### 4. `[POST][User] wishlist/add_no_size/<user_id>/<product_id>` добавить товара "без размера"

Response: карточку вишлиста
<a name="change_wl"></a>

### 5. `[POST][User] wishlist/change_size/<user_id>/<wishlist_unit_id>/<size_id>` поменять размер в вишлисте

Response: карточку вишлиста
[:arrow_up:WishList API](#wishlist)
[:arrow_up:SellOut API](#up)

<a name="orders"></a>

## Orders API

[:arrow_up:SellOut API](#up)
<a name="cart"></a>

### 1. `[GET][User] order/cart/<user_id>` корзина пользователя

Response:

```json
{
  "id": 1,
  "user": {
    "id": 1,
    "last_login": "2023-04-12T15:14:50.148633Z",
    "is_superuser": true,
    "username": "artem",
    "first_name": "",
    "last_name": "",
    "email": "arten@mail.ru",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2023-04-07T15:26:38Z",
    "all_purchase_amount": 0,
    "personal_discount_percentage": 0,
    "referral_link": null,
    "preferred_size_grid": null,
    "gender": null,
    "ref_user": null,
    "groups": [],
    "user_permissions": [],
    "my_groups": [],
    "address": [],
    "last_viewed_products": [
      {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      },
      {
        "id": 2,
        "name": "Dunk",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "sku",
        "available_flag": true,
        "last_upd": "2023-04-07T15:59:39Z",
        "add_date": "2023-04-07",
        "fit": 0,
        "rel_num": 0,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      }
    ]
  },
  "product_units": [
    {
      "id": 1,
      "final_price": 7,
      "availability": true,
      "product": {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      },
      "size": {
        "id": 1,
        "INT": "12",
        "US": "12",
        "UK": "12",
        "EU": "12",
        "IT": "12",
        "RU": "12",
        "product": 1
      },
      "currency": {
        "id": 2,
        "name": "pending"
      },
      "delivery_type": {
        "id": 1,
        "name": "Самолёт"
      },
      "platform": {
        "id": 1,
        "platform": "Poizon",
        "site": "/poizon"
      }
    }
  ]
}
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)
<a name="add_to_cart"></a>

### 2. `[POST][User] order/cart_add/<user_id>/<product_unit_id>` добавить юнит в корзину

Response:

```json
{
  "id": 2,
  "final_price": 100,
  "availability": true,
  "product": {
    "id": 2,
    "name": "Dunk",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "sku",
    "available_flag": true,
    "last_upd": "2023-04-07T15:59:39Z",
    "add_date": "2023-04-07",
    "fit": 0,
    "rel_num": 0,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ]
  },
  "size": {
    "id": 1,
    "INT": "12",
    "US": "12",
    "UK": "12",
    "EU": "12",
    "IT": "12",
    "RU": "12",
    "product": {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": 1,
      "brands": [
        1
      ],
      "categories": [
        1
      ],
      "tags": [
        1
      ]
    }
  },
  "currency": {
    "id": 2,
    "name": "pending"
  },
  "delivery_type": {
    "id": 1,
    "name": "Самолёт"
  },
  "platform": {
    "id": 1,
    "platform": "Poizon",
    "site": "/poizon"
  }
}
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)
<a name="del_from_cart"></a>

### 3. `[DELETE][User] order/cart_delete/<user_id>/<product_unit_id>` удалить юнит из корзины

Response:

```json
{
  "id": 2,
  "final_price": 100,
  "availability": true,
  "product": {
    "id": 2,
    "name": "Dunk",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "sku",
    "available_flag": true,
    "last_upd": "2023-04-07T15:59:39Z",
    "add_date": "2023-04-07",
    "fit": 0,
    "rel_num": 0,
    "gender": {
      "id": 1,
      "name": "M"
    },
    "brands": [
      {
        "id": 1,
        "name": "Nike"
      }
    ],
    "categories": [
      {
        "id": 1,
        "name": "Sport"
      }
    ],
    "tags": [
      {
        "id": 1,
        "name": "Style"
      }
    ]
  },
  "size": {
    "id": 1,
    "INT": "12",
    "US": "12",
    "UK": "12",
    "EU": "12",
    "IT": "12",
    "RU": "12",
    "product": {
      "id": 1,
      "name": "Air Force 1",
      "bucket_link": "/buck",
      "description": "desc",
      "sku": "air_force_1",
      "available_flag": true,
      "last_upd": "2023-04-07T15:28:17Z",
      "add_date": "2023-04-07",
      "fit": 1,
      "rel_num": 1,
      "gender": 1,
      "brands": [
        1
      ],
      "categories": [
        1
      ],
      "tags": [
        1
      ]
    }
  },
  "currency": {
    "id": 2,
    "name": "pending"
  },
  "delivery_type": {
    "id": 1,
    "name": "Самолёт"
  },
  "platform": {
    "id": 1,
    "platform": "Poizon",
    "site": "/poizon"
  }
}
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)
<a name="checkout"></a>

### 4. `[POST][User] order/checkout/<user_id>` оформить заказ

Body:

```json
{
  "product_unit": [
    1,
    2
  ],
  "email": "mail@mail.ru",
  "tel": 77777777777,
  "first_name": "Имя",
  "last_name": "Фамилия",
  "address_id": 1,
  "promo_code": "SALE",
  "total_amount": 10000
}
```

Response:

```json
{
  "id": 13,
  "total_amount": 10000,
  "email": "mail@mail.ru",
  "tel": "77777777777",
  "name": "Имя",
  "surname": "Фамилия",
  "fact_of_payment": false,
  "user": {
    "id": 1,
    "last_login": "2023-04-12T15:14:50.148633Z",
    "is_superuser": true,
    "username": "artem",
    "first_name": "",
    "last_name": "",
    "email": "arten@mail.ru",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2023-04-07T15:26:38Z",
    "all_purchase_amount": 0,
    "personal_discount_percentage": 0,
    "referral_link": null,
    "preferred_size_grid": null,
    "gender": null,
    "ref_user": null,
    "groups": [],
    "user_permissions": [],
    "my_groups": [],
    "address": [],
    "last_viewed_products": [
      {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      },
      {
        "id": 2,
        "name": "Dunk",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "sku",
        "available_flag": true,
        "last_upd": "2023-04-07T15:59:39Z",
        "add_date": "2023-04-07",
        "fit": 0,
        "rel_num": 0,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      }
    ]
  },
  "address": {
    "id": 1,
    "address": "Проспект Мира 111",
    "post_index": "308033"
  },
  "promo_code": {
    "id": 1,
    "string_representation": "SALE",
    "discount_percentage": 15,
    "discount_absolute": 0,
    "activation_count": 6,
    "max_activation_count": 10,
    "active_status": true,
    "active_until_date": "2023-04-18",
    "owner": {
      "id": 1,
      "last_login": "2023-04-12T15:14:50.148633Z",
      "is_superuser": true,
      "username": "artem",
      "first_name": "",
      "last_name": "",
      "email": "arten@mail.ru",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2023-04-07T15:26:38Z",
      "all_purchase_amount": 0,
      "personal_discount_percentage": 0,
      "referral_link": null,
      "preferred_size_grid": null,
      "gender": null,
      "ref_user": null,
      "groups": [],
      "user_permissions": [],
      "my_groups": [],
      "address": [],
      "last_viewed_products": [
        1,
        2
      ]
    }
  },
  "status": {
    "id": 1,
    "name": "pending"
  },
  "product_unit": [
    {
      "id": 1,
      "final_price": 7,
      "availability": true,
      "product": {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      },
      "size": {
        "id": 1,
        "INT": "12",
        "US": "12",
        "UK": "12",
        "EU": "12",
        "IT": "12",
        "RU": "12",
        "product": 1
      },
      "currency": {
        "id": 2,
        "name": "pending"
      },
      "delivery_type": {
        "id": 1,
        "name": "Самолёт"
      },
      "platform": {
        "id": 1,
        "platform": "Poizon",
        "site": "/poizon"
      }
    },
    {
      "id": 2,
      "final_price": 100,
      "availability": true,
      "product": {
        "id": 2,
        "name": "Dunk",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "sku",
        "available_flag": true,
        "last_upd": "2023-04-07T15:59:39Z",
        "add_date": "2023-04-07",
        "fit": 0,
        "rel_num": 0,
        "gender": 1,
        "brands": [
          1
        ],
        "categories": [
          1
        ],
        "tags": [
          1
        ]
      },
      "size": {
        "id": 1,
        "INT": "12",
        "US": "12",
        "UK": "12",
        "EU": "12",
        "IT": "12",
        "RU": "12",
        "product": 1
      },
      "currency": {
        "id": 2,
        "name": "pending"
      },
      "delivery_type": {
        "id": 1,
        "name": "Самолёт"
      },
      "platform": {
        "id": 1,
        "platform": "Poizon",
        "site": "/poizon"
      }
    }
  ]
}
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)

<a name="orderss"></a>

### 5. `[GET][Admin] order/orders` все заказы [Вниз к запросу](#orders)

Response:

```json
[
  {
    "id": 1,
    "user": {
      "id": 1,
      "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
      "last_login": "2023-04-21T14:57:10.100840Z",
      "is_superuser": true,
      "username": "artem",
      "first_name": "",
      "last_name": "",
      "email": "arten@mail.ru",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2023-04-07T15:26:38Z",
      "all_purchase_amount": 0,
      "personal_discount_percentage": 0,
      "referral_link": null,
      "preferred_size_grid": null,
      "gender": null,
      "ref_user": null,
      "groups": [],
      "user_permissions": [],
      "my_groups": [],
      "address": [],
      "last_viewed_products": [
        {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        }
      ]
    },
    "product_units": [
      {
        "id": 1,
        "final_price": 7,
        "availability": true,
        "product": {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      },
      {
        "id": 2,
        "final_price": 100,
        "availability": true,
        "product": {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      }
    ]
  },
  {
    "id": 2,
    "user": {
      "id": 2,
      "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
      "last_login": "2023-04-12T10:07:07Z",
      "is_superuser": false,
      "username": "noadmin",
      "first_name": "no",
      "last_name": "admin",
      "email": "noadmin@mail.ru",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2023-04-12T10:07:34Z",
      "all_purchase_amount": 0,
      "personal_discount_percentage": 0,
      "referral_link": null,
      "preferred_size_grid": null,
      "gender": null,
      "ref_user": null,
      "groups": [],
      "user_permissions": [],
      "my_groups": [],
      "address": [],
      "last_viewed_products": [
        {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        }
      ]
    },
    "product_units": [
      {
        "id": 1,
        "final_price": 7,
        "availability": true,
        "product": {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      }
    ]
  }
]
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)

<a name="user_orders"></a>

### 6. `[GET][User] order/user_orders/<user_id>` все заказы пользователя

Response:

```json
[
  {
    "id": 2,
    "total_amount": 107,
    "email": "sh@mail.ru",
    "tel": "7777777777777",
    "name": "artem",
    "surname": "sh",
    "fact_of_payment": false,
    "user": {
      "id": 2,
      "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
      "last_login": "2023-04-12T10:07:07Z",
      "is_superuser": false,
      "username": "noadmin",
      "first_name": "no",
      "last_name": "admin",
      "email": "noadmin@mail.ru",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2023-04-12T10:07:34Z",
      "all_purchase_amount": 0,
      "personal_discount_percentage": 0,
      "referral_link": null,
      "preferred_size_grid": null,
      "gender": null,
      "ref_user": null,
      "groups": [],
      "user_permissions": [],
      "my_groups": [],
      "address": [],
      "last_viewed_products": [
        {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        }
      ]
    },
    "address": {
      "id": 1,
      "address": "Проспект Мира 111",
      "post_index": "308033"
    },
    "promo_code": null,
    "status": {
      "id": 1,
      "name": "pending"
    },
    "product_unit": [
      {
        "id": 1,
        "final_price": 7,
        "availability": true,
        "product": {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      },
      {
        "id": 2,
        "final_price": 100,
        "availability": true,
        "product": {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      }
    ]
  }
]
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)

<a name="order"></a>

### 7. `[GET][User] order/info/<order_id>` информация о заказе

Response:

```json
[
  {
    "id": 2,
    "total_amount": 107,
    "email": "sh@mail.ru",
    "tel": "7777777777777",
    "name": "artem",
    "surname": "sh",
    "fact_of_payment": false,
    "user": {
      "id": 2,
      "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
      "last_login": "2023-04-12T10:07:07Z",
      "is_superuser": false,
      "username": "noadmin",
      "first_name": "no",
      "last_name": "admin",
      "email": "noadmin@mail.ru",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2023-04-12T10:07:34Z",
      "all_purchase_amount": 0,
      "personal_discount_percentage": 0,
      "referral_link": null,
      "preferred_size_grid": null,
      "gender": null,
      "ref_user": null,
      "groups": [],
      "user_permissions": [],
      "my_groups": [],
      "address": [],
      "last_viewed_products": [
        {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        }
      ]
    },
    "address": {
      "id": 1,
      "address": "Проспект Мира 111",
      "post_index": "308033"
    },
    "promo_code": null,
    "status": {
      "id": 1,
      "name": "pending"
    },
    "product_unit": [
      {
        "id": 1,
        "final_price": 7,
        "availability": true,
        "product": {
          "id": 1,
          "name": "Air Force 1",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "air_force_1",
          "available_flag": true,
          "last_upd": "2023-04-07T15:28:17Z",
          "add_date": "2023-04-07",
          "fit": 1,
          "rel_num": 1,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      },
      {
        "id": 2,
        "final_price": 100,
        "availability": true,
        "product": {
          "id": 2,
          "name": "Dunk",
          "bucket_link": "/buck",
          "description": "desc",
          "sku": "sku",
          "available_flag": true,
          "last_upd": "2023-04-07T15:59:39Z",
          "add_date": "2023-04-07",
          "fit": 0,
          "rel_num": 0,
          "gender": 1,
          "brands": [
            1
          ],
          "categories": [
            1
          ],
          "tags": [
            1
          ]
        },
        "size": {
          "id": 1,
          "INT": "12",
          "US": "12",
          "UK": "12",
          "EU": "12",
          "IT": "12",
          "RU": "12",
          "product": 1
        },
        "currency": {
          "id": 2,
          "name": "pending"
        },
        "delivery_type": {
          "id": 1,
          "name": "Самолёт"
        },
        "platform": {
          "id": 1,
          "platform": "Poizon",
          "site": "/poizon"
        }
      }
    ]
  }
]
```

[:arrow_up:Orders API](#orders)
[:arrow_up:SellOut API](#up)