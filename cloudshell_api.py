import sys

from cloudshell.api.cloudshell_api import CloudShellAPISession

server_ip = sys.argv[1]
reservation_id = sys.argv[2]
DEPLOYED_APP_MODEL = 'Generic App Model'

session = CloudShellAPISession(server_ip,
                               sys.argv[3],
                               sys.argv[4],
                               sys.argv[5])


resources = session.GetReservationDetails(reservation_id).ReservationDescription.Resources

my_resource = [resource for resource in resources
               if resource.ResourceModelName == DEPLOYED_APP_MODEL]

if len(my_resource) > 1:
    raise Exception('There are more then one app in the sandbox')

if len(my_resource) == 0:
    raise Exception('There are no deployed application in the sandbox')

resource_att = session.GetResourceDetails(my_resource[0].Name).ResourceAttributes
for item in resource_att:
    if item.Name == 'Public IP':
	sys.stdout.write(item.Value)
        break