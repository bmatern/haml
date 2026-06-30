import argparse
import xmlschema

def validate_against_schema(schema_filename, xml_filename):
    schema = xmlschema.XMLSchema11(schema_filename)
    if schema.is_valid(xml_filename):
        print("Valid XML!")
    else:
        schema.validate(xml_filename) # Throws detailed error


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-xml", "--xml", help="Path to the XML file", required=True, type=str)
    parser.add_argument("-xsd", "--xsd", help="Path to the XSD Schema file", required=True, type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    validate_against_schema(schema_filename=args.xsd
                            , xml_filename=args.xml)

if __name__ == '__main__':
    main()