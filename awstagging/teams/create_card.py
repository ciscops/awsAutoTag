import json
from jinja2 import Environment, PackageLoader
from pyadaptivecards.components import TextBlock, Fact, Column, Choice
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Choices
from pyadaptivecards.actions import Submit
from pyadaptivecards.options import FontSize, HorizontalAlignment, Colors
from pyadaptivecards.container import FactSet, ColumnSet

CONTENT_TYPE = "application/vnd.microsoft.card.adaptive"


def create_two_col_card(device, greetingtext, fields, time):
    greeting = TextBlock(greetingtext,
                         size=FontSize.LARGE,
                         horizontalAlignment=HorizontalAlignment.CENTER,
                         color=Colors.ACCENT)
    col1 = []
    col2 = []
    for field in fields:
        name = field[0]
        value = field[1]
        col1.append(TextBlock(text=str(name), size=FontSize.SMALL))
        col2.append(TextBlock(text=str(device[value]), size=FontSize.SMALL))

    col1.append(TextBlock(text=str('As Of'), size=FontSize.SMALL))
    col2.append(TextBlock(text=str(time), size=FontSize.SMALL))
    column1 = Column(items=col1)
    column2 = Column(items=col2)
    table = ColumnSet(columns=[column1, column2])
    card = AdaptiveCard(body=[greeting, table])
    attachment = {
        "contentType": CONTENT_TYPE,
        "content": card.to_dict(),
    }
    print(card.to_json(pretty=True))
    return attachment


def create_update_instance_tag_card(tags, instanceid):

    _greeting = TextBlock(f"New EC2 Instance ID: {str(instanceid)}  "
                          f"Has Been Created Please Validate Your Tags",
                          horizontalAlignment=HorizontalAlignment.CENTER,
                          size=FontSize.SMALL)

    _choices = [
        Choice("Cisco Restricted", "Cisco Restricted"),
        Choice("Cisco Highly Confidentia", "Cisco Highly Confidentia")
    ]
    _data_classification = Choices(id="Data Classification",
                                   choices=_choices,
                                   value=str(tags.dataclassification),
                                   style=2)

    _choices = [Choice("dev", "dev"), Choice("test", "test"), Choice("stage", "stage"), Choice("prod", "prod")]
    _environment = Choices(id="Environment", choices=_choices, value=str(tags.environment), style=2)

    _resourc_oewner = Text('Resource Owner', value=str(tags.resourceowner))

    _cisco_mail_alias = Text("Cisco Mail Alias", value=str(tags.ciscomailalias))

    _choices = [Choice("Cisco Operations Data", "Cisco Operations Data")]
    _data_taxonomy = Choices(id="Data Taxonomy", choices=_choices, value=str(tags.datataxonomy), style=2)

    _app_name = Text("Application Name", value=str(tags.appname))

    _footer = TextBlock("Security Tags must be validated with in 24 hours "
                        "or your EC2 instace will be terminated",
                        horizontalAlignment=HorizontalAlignment.CENTER,
                        size=FontSize.SMALL,
                        color=Colors.ATTENTION)

    submit = Submit(title="Update", data={"instid": instanceid})
    card = AdaptiveCard(body=[
        _greeting, _app_name, _resourc_oewner, _cisco_mail_alias, _environment, _data_classification, _data_taxonomy,
        _footer
    ],
                        actions=[submit])
    attachment = {
        "contentType": CONTENT_TYPE,
        "content": card.to_dict(),
    }

    print(card.to_json(pretty=True))
    return attachment


def static_new_instance(tags, instanceid):

    greeting = TextBlock(f"New EC2 Instance ID: {str(instanceid)}  "
                         f"Has Been Created Please Validate Your Tags",
                         horizontalAlignment=HorizontalAlignment.CENTER,
                         size=FontSize.LARGE)

    _data_classification = Fact(title="Data Classification", value=str(tags.dataclassification))
    _environment = Fact(title='Environment', value=str(tags.environment))
    _resourc_oewner = Fact(title='ResourceOwner', value=str(tags.resourceowner))
    _cisco_mail_alias = Fact(title="Cisco Mail Alias", value=str(tags.ciscomailalias))
    _data_taxonomy = Fact(title="Data Taxonomy", value=str(tags.datataxonomy))
    _app_name = Fact(title="Application Name", value=str(tags.appname))
    info = FactSet(
        facts=[_data_classification, _environment, _resourc_oewner, _cisco_mail_alias, _data_taxonomy, _app_name])
    approve = Submit(title="Approve", data={"instid": instanceid})
    card = AdaptiveCard(body=[greeting, info], actions=[approve])
    attachment = {
        "contentType": CONTENT_TYPE,
        "content": card.to_dict(),
    }
    return attachment


def template_card(file, data):
    _env = Environment(loader=PackageLoader('teams', 'templates'))
    _env.filters['jsonify'] = json.dumps

    #Templte file ./teams/templates/<template>
    template = _env.get_template(file)
    attachment = template.render(data=data)

    return json.loads(attachment)
