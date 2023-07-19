#!/bin/bash

# Create account directory
mkdir account
cd account

# Create application directory
mkdir application
touch application/__init__.py
touch application/account_service.py
touch application/account_repository.py

# Create domain directory
mkdir domain
touch domain/__init__.py
touch domain/account.py
touch domain/value_objects.py

# Create infrastructure directory
mkdir infrastructure
touch infrastructure/__init__.py
touch infrastructure/account_repository_impl.py
touch infrastructure/database.py

# Create __init__.py file for the account directory
touch __init__.py
