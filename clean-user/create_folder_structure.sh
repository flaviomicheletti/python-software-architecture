#!/bin/bash

# Create directories
mkdir app
mkdir app/entities
mkdir app/usecases
mkdir app/interfaces
mkdir app/adapters

# Create entity file
touch app/entities/user.py

# Create use case file
touch app/usecases/create_user.py

# Create input/output port files
touch app/interfaces/input_ports.py
touch app/interfaces/output_ports.py
touch app/interfaces/repositories.py

# Create input/output adapter files
touch app/adapters/input_adapters.py
touch app/adapters/output_adapters.py

# Create main.py file
touch main.py

echo "Folder structure and files created successfully!"
