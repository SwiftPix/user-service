import re
from marshmallow import Schema, fields, validate, ValidationError

def validate_password_complexity(password):
    if len(password) < 8:
        raise ValidationError("A senha deve ter no mínimo 8 caracteres")
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError("A senha deve conter pelo menos uma letra maiúscula")
    
    if not re.search(r'\d', password):
        raise ValidationError("A senha deve conter pelo menos um número")
    
    if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
        raise ValidationError("A senha deve conter pelo menos um caractere especial")

class UserSchema(Schema):
    name = fields.Str(required=True, 
                               validate=validate.Length(min=1, error="O nome completo é obrigatório"))
    
    email = fields.Email(required=True, 
                         error_messages={"required": "O endereço de e-mail é obrigatório", 
                                         "invalid": "O endereço de e-mail fornecido não é válido"})
    
    cellphone = fields.Str(required=True, 
                                 validate=validate.Regexp(r'^\+?\d+$', 
                                                         error="O número de telefone deve conter apenas dígitos"))
    
    password = fields.Str(required=True, 
                       validate=[validate.Length(min=8, error="A senha deve ter no mínimo 8 caracteres"),
                                 validate_password_complexity])
    
class LoginSchema(Schema):
    email = fields.Email(required=True, 
                         error_messages={"required": "O endereço de e-mail é obrigatório", 
                                         "invalid": "O endereço de e-mail fornecido não é válido"})
    
    password = fields.Str(required=True, 
                                validate=validate.Length(min=1, error="A senha é obrigatória"))
