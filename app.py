from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.containerinstance.models import ContainerGroup

# Parameters (these will be passed when the runbook is executed)
RESOURCE_GROUP_NAME = 'zep-resource-group'
CONTAINER_GROUP_NAME = 'zep-continst'
ACTION = 'Start'  # Change to 'Stop' to stop the container

# Authenticate using the Azure Automation Run As account or Managed Identity
credential = DefaultAzureCredential()
subscription_id = 'c1b6f5f6-8d55-4b87-b621-49a0c0a22c2b'  # replace with your subscription ID

# Create a client
client = ContainerInstanceManagementClient(credential, subscription_id)

# Function to start the container group
def start_container_group():
    print(f"Starting container group: {CONTAINER_GROUP_NAME}")
    client.container_groups.start(RESOURCE_GROUP_NAME, CONTAINER_GROUP_NAME)

# Function to stop the container group
def stop_container_group():
    print(f"Stopping container group: {CONTAINER_GROUP_NAME}")
    client.container_groups.stop(RESOURCE_GROUP_NAME, CONTAINER_GROUP_NAME)

# Main logic
if ACTION == 'Start':
    start_container_group()
elif ACTION == 'Stop':
    stop_container_group()
else:
    print("Invalid action. Please specify 'Start' or 'Stop'.")

