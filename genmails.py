import re

def generate_email_patterns(first_name, middle_name, last_name, company_name, extension=None):
    first_initial = first_name[0].lower()
    middle_initial = middle_name[0].lower() if middle_name else ""
    last_initial = last_name[0].lower()
    first_name = first_name.lower()
    middle_name = middle_name.lower() if middle_name else ""
    last_name = last_name.lower()
    company_name = company_name.lower()

    # Define possible extensions
    default_extensions = ['com', 'in']
    if extension and extension not in default_extensions:
        # Use user-defined extension
        extensions = [extension]
    else:
        # Use default extensions
        extensions = default_extensions

    # Define common and other patterns
    common_patterns = [
        f"{first_name}.{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{last_name}@{company_name}.{{ext}}",
        f"{first_name}{last_name}@{company_name}.{{ext}}",
        f"{first_name}@{company_name}.{{ext}}",
        f"{last_name}@{company_name}.{{ext}}",
        f"{first_initial}.{last_name}@{company_name}.{{ext}}",
        f"{first_name}-{last_name}@{company_name}.{{ext}}",
        f"{last_name}{first_name}{middle_name}@{company_name}.{{ext}}",
        f"{first_name}{middle_name}{last_name}@{company_name}.{{ext}}",
    ]
    
    other_patterns = [
        f"{first_name}.{middle_name}.{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_initial}{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_initial}{last_initial}@{company_name}.{{ext}}",
        f"{first_name}.{middle_initial}.{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_name}{last_name}@{company_name}.{{ext}}",
        f"{first_name}.{middle_initial}@{company_name}.{{ext}}",
        f"{first_initial}{middle_name}@{company_name}.{{ext}}",
        f"{middle_name}.{last_name}@{company_name}.{{ext}}",
        f"{first_name}.{last_initial}@{company_name}.{{ext}}",
        f"{first_initial}{last_initial}@{company_name}.{{ext}}",
        f"{first_initial}_{last_name}@{company_name}.{{ext}}",
        f"{last_name}.{first_name}@{company_name}.{{ext}}",
        f"{last_name}.{first_initial}@{company_name}.{{ext}}",
        f"{first_name}-{last_initial}@{company_name}.{{ext}}",
        f"{first_name}_{last_initial}@{company_name}.{{ext}}",
        f"{first_name}.{middle_name}.{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_initial}.{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_initial}-{last_name}@{company_name}.{{ext}}",
        f"{first_name}-{middle_initial}.{last_name}@{company_name}.{{ext}}",
        f"{first_name}.{middle_name}{last_name}@{company_name}.{{ext}}",
        f"{first_initial}{middle_name}.{last_name}@{company_name}.{{ext}}",
        f"{last_name}.{middle_name}@{company_name}.{{ext}}",
        f"{middle_name}-{last_name}@{company_name}.{{ext}}",
        f"{first_name}.{middle_initial}@{company_name}.{{ext}}",
        f"{middle_initial}.{last_name}@{company_name}.{{ext}}",
    ]

    # Remove duplicates from common and other patterns
    unique_common_patterns = list(set(common_patterns))
    unique_other_patterns = list(set(other_patterns) - set(unique_common_patterns))
    
    # Apply extensions
    email_patterns = []
    for ext in extensions:
        for pattern in unique_common_patterns + unique_other_patterns:
            email_patterns.append(pattern.format(ext=ext))
    
    return email_patterns

def is_valid_email(email):
    # Define a more robust regex pattern for a valid email address
    email_regex = re.compile(
        r"^(?![.-])(?:(?:[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*)|(?:[._-][a-zA-Z0-9]+))@(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}|(?:[a-zA-Z0-9-]+\.[a-zA-Z]{2,}))$"
    )
    return email_regex.match(email) is not None

def main():
    first_name = input("Enter the first name: ")
    middle_name = input("Enter the middle name (if any, otherwise leave blank): ")
    last_name = input("Enter the last name: ")
    company_name = input("Enter the company name: ")
    
    # Prompt user for extension
    extension = input("Enter the extension (com, in, org, net, edu etc... leave blank for default): ").strip().lower()

    # Generate email patterns
    email_patterns = generate_email_patterns(first_name, middle_name, last_name, company_name, extension if extension else None)

    print("\nGenerated Valid Email Addresses:")
    for pattern in email_patterns:
        if is_valid_email(pattern):
            print(pattern)

if __name__ == "__main__":
    main()
