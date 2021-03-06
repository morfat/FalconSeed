import math
import falcon
import jsonschema


class Table(object):
    pk=None
    name="" # db table name
    properties={} #schema properties
    schema={} #to hold schema for each model
    required=[] #list of required fields
    


    def __init__(self):
        self.validated_data={}
        self.read_only=[]
        self.write_only=[]


    def get_schema(self):
        #get schema by providing required fields. Provideed as a list. e.g ["id","name"]
        self.schema.update({"properties":self.properties,'required':self.required,"title":self.name,"type": "object"})
        return self.schema

   
    def validate(self,data):
        try:
            schema=self.get_schema()
            jsonschema.validate(data, self.get_schema(), format_checker=jsonschema.FormatChecker())
            #if above passes
            properties=schema.get('properties')
            for k,v in properties.items():
                if v.get('readOnly'):
                    self.read_only.append(k)
                if v.get('writeOnly'):
                    self.write_only.append(k)
            #remove items in data that are not in schema properties
            self.validated_data={k:v for k,v in data.items() if properties.get(k)}
        except jsonschema.ValidationError as e:
            raise falcon.HTTPBadRequest('Data validation failed',description=e.message)

    def get_cleaned_data(self):
        return {k:v for k,v in self.validated_data.items() if k not in self.read_only}

    def get_display_data(self):
        return {k:v for k,v in self.validated_data.items() if k not in self.write_only}

    def get_display_fields(self):
        return [k for k,v in self.properties.items() if v.get('writeOnly') is not True]


    











        












