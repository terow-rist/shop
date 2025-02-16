# shop
This is a simple FastAPI-based shop API that allows users to manage products, users, and orders. It connects to a MongoDB database using `motor` for async operations.

## Features
- CRUD operations for **Products**, **Users**, and **Orders**
- Data validation using `pydantic`
- MongoDB integration using `motor`
- Role-based validation for users
- Order status validation

## Installation

### Prerequisites
- Python 3.8+
- MongoDB running locally or remotely
- `pip` package manager

### Setup
1. Clone the repository:
   ```sh
   git clone git@github.com:terow-rist/shop.git
   cd shop
   ```
2. Create a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file in the root directory and add:
   ```env
   MONGO_URI=mongodb://localhost:27017
   ```
5. Run the application using `uvicorn`:
   ```sh
   uvicorn main:app --reload
   ```

   The `--reload` flag enables auto-reloading of the app during development.

6. Open the API documentation by navigating to:
   ```
   http://127.0.0.1:8000/docs
   or
   https://shop-zj5o.onrender.com/docs
   ```

   Here, you can explore the available endpoints and test them.

## API Endpoints

### Products
| Method | Endpoint           | Description                  |
|--------|-------------------|------------------------------|
| POST   | `/products/`       | Create a new product        |
| GET    | `/products/{id}`   | Retrieve a product by ID    |
| PUT    | `/products/{id}`   | Update a product by ID      |
| DELETE | `/products/{id}`   | Delete a product by ID      |

### Users
| Method | Endpoint           | Description                  |
|--------|-------------------|------------------------------|
| POST   | `/users/`         | Register a new user         |
| GET    | `/users/{id}`     | Retrieve user by ID         |
| PUT    | `/users/{id}`     | Update user by ID          |
| DELETE | `/users/{id}`     | Delete user by ID          |

### Orders
| Method | Endpoint           | Description                  |
|--------|-------------------|------------------------------|
| POST   | `/orders/`        | Create a new order          |
| GET    | `/orders/{user}`  | Retrieve orders by user ID  |
| PUT    | `/orders/{id}`    | Update an order by ID       |
| DELETE | `/orders/{id}`    | Delete an order by ID       |


## License
This project is open-source and available under the MIT License.
