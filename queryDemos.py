
customers = Customer.objects.all()
order = Order.objects.first() 
parentName = order.customer.name


leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 



allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.all()
#Returns all child models related to parent
parent.childmodel_set.all()

