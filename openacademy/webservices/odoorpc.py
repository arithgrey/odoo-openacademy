import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)

# Check available databases
print(odoo.db.list())

# Login
odoo.login('odoo-db', 'admin', 'admin')

# Current user
user = odoo.env.user
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

