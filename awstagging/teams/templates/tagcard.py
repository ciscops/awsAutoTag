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
                    "type": "Input.Text",
                    "placeholder": data.appname,
                    "id": "appname",
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
                        "title": "Cisco Operations Data",
                        "value": "Cisco Operations Data"
                    }],
                    "id":
                    "datataxonomy",
                    "type":
                    "Input.ChoiceSet",
                    "value":
                    data.datataxonomy
                }, {
                    "type":
                    "ActionSet",
                    "actions": [{
                        "type": "Action.Submit",
                        "title": "Approve"
                    }],
                    "horizontalAlignment":
                    "Center"
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
                "type": "Action.Submit"
            }
        }]
    }
    return CARD_CONTENT
