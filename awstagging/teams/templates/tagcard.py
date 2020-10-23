def build_card(data):
    CARD_CONTENT = {
        "$schema":
        "http://adaptivecards.io/schemas/adaptive-card.json",
        "type":
        "AdaptiveCard",
        "version":
        "1.1",
        "body": [{
            "type": "TextBlock",
            "text":
            f'New EC2 Instance ID: {data.itemid} has been created please validate your tags',
            "size": "Medium",
            "color": "Dark",
            "wrap": True,
            "maxLines": 2,
            "horizontalAlignment": "Center"
        }, {
            "type":
            "ColumnSet",
            "columns": [{
                "type":
                "Column",
                "width":
                "stretch",
                "items": [{
                    "type": "TextBlock",
                    "text": "Application Name",
                    "horizontalAlignment": "Left",
                    "size": "Small"
                }, {
                    "id": "appname",
                    "type": "Input.Text",
                    "value": data.appname,
                    "spacing": "None"
                }, {
                    "type": "TextBlock",
                    "text": "Resource Owner",
                    "size": "Small",
                    "horizontalAlignment": "Left"
                }, {
                    "id": "resourceowner",
                    "type": "Input.Text",
                    "value": data.resourceowner,
                    "spacing": "None"
                }, {
                    "type": "TextBlock",
                    "text": "Cisco Mail Alias",
                    "size": "Small",
                    "horizontalAlignment": "Left"
                }, {
                    "id": "ciscomailalias",
                    "type": "Input.Text",
                    "value": data.ciscomailalias,
                    "spacing": "None"
                }, {
                    "type": "TextBlock",
                    "text": "Environments",
                    "size": "Small",
                    "horizontalAlignment": "Left"
                }, {
                    "choices": [{
                        "title": "dev",
                        "value": "dev"
                    }, {
                        "title": "test",
                        "value": "test"
                    }, {
                        "title": "stage",
                        "value": "stage"
                    }, {
                        "title": "prod",
                        "value": "prod"
                    }],
                    "id":
                    "environment",
                    "type":
                    "Input.ChoiceSet",
                    "value":
                    data.environment
                }, {
                    "type": "TextBlock",
                    "text": "Data Classification",
                    "size": "Small",
                    "horizontalAlignment": "Left"
                }, {
                    "choices": [{
                        "title": "Cisco Restricted",
                        "value": "Cisco Restricted"
                    }, {
                        "title": "Cisco Highly Confidentia",
                        "value": "Cisco Highly Confidentia"
                    }, {
                        "title": "Cisco Confidential",
                        "value": "Cisco Confidential"
                    }, {
                        "title": "Cisco Public",
                        "value": "Cisco Public"
                    }],
                    "id":
                    "dataclassification",
                    "type":
                    "Input.ChoiceSet",
                    "value":
                    data.dataclassification
                }, {
                    "type": "TextBlock",
                    "text": "Data Taxonomy",
                    "size": "Small",
                    "horizontalAlignment": "Left"
                }, {
                    "choices": [{
                        "title": "Administrative Data",
                        "value": "Administrative Data"
                    }, {
                        "title": "Customer Data",
                        "value": "Customer Data"
                    }, {
                        "title": "Entrusted Data",
                        "value": "Entrusted Data"
                    }, {
                        "title": "Financing Data",
                        "value": "Financing Data"
                    }, {
                        "title": "Support Data",
                        "value": "Support Data"
                    }, {
                        "title": "Telemetry Data",
                        "value": "Telemetry Data"
                    }, {
                        "title": "Cisco Operations Data",
                        "value": "Cisco Operations Data"
                    }, {
                        "title": "Cisco Strategic Data",
                        "value": "Cisco Strategic Data"
                    }, {
                        "title": "Human Resources Data",
                        "value": "Human Resources Data"
                    }],
                    "id":
                    "datataxonomy",
                    "type":
                    "Input.ChoiceSet",
                    "value":
                    data.datataxonomy
                }, {
                    "id": "leaverunning",
                    "type": "Input.Toggle",
                    "title": "Leave Running",
                    "value": "false",
                    "wrap": True
                }, {
                    "type":
                    "ActionSet",
                    "actions": [{
                        "type": "Action.Submit",
                        "title": "Approve"
                    }],
                    "horizontalAlignment": "Center"
                }, {
                    "type": "TextBlock",
                    "text":
                    "Security Tags must be validated within 24 hours or your EC2 instance will be terminated",
                    "horizontalAlignment": "Center",
                    "size": "Small",
                    "color": "Attention",
                    "wrap": True
                }]
            }],
            "selectAction": {
                "type": "Action.Submit",
                "data": {
                    "itemid": data.itemid,
                    "approved": "True"
                }
            }
        }]
    }
    return CARD_CONTENT
