# Seed Command for Listings

This directory contains a Django management command to populate the database with sample listings data for development and testing.

## Usage

To seed your database with sample listings, run the following command from your project root:

```bash
python manage.py seed
```

## What It Does

- Adds sample listings to the database if they do not already exist.
- Useful for quickly setting up test data.

## Sample Data

- Cozy Apartment in Nairobi
- Beach House in Mombasa
- Mountain Cabin in Nyeri

## Notes

- The command uses `get_or_create` to avoid duplicate entries.
- You can modify `seed.py` to add more sample data as needed.