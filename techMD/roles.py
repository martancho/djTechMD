from rolepermissions.roles import AbstractUserRole

class Associate_Engineer(AbstractUserRole):
	available_permissions = {
		'create_record':True,
	}


class Lead_Engineer(AbstractUserRole):
	available_permissions = {

	}

class Manager(AbstractUserRole):
	available_permissions = {

	}

class Purchaser(AbstractUserRole):
	available_permissions = {
	
	}
