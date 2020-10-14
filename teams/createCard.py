from pyadaptivecards.components import TextBlock, Fact,Column
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text
from pyadaptivecards.actions import Submit
from pyadaptivecards.options import FontSize,HorizontalAlignment,Colors,VerticalContentAlignment
from pyadaptivecards.container import FactSet,ColumnSet




def createTwoColCard(device,greetingtext,fields,time):
    greeting = TextBlock(greetingtext, size=FontSize.LARGE,
        horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.ACCENT)
    col1=[]
    col2=[]
    for field  in fields:
        name = field[0]
        value = field[1]
        col1.append(TextBlock(text=str(name),
                                           size=FontSize.SMALL))
        col2.append(TextBlock(text=str(device[value]),
                                           size=FontSize.SMALL))

    col1.append(TextBlock(text=str('As Of'),
                                       size=FontSize.SMALL))
    col2.append(TextBlock(text=str(time),
                                       size=FontSize.SMALL))
    column1 = Column(items=col1)
    column2 = Column(items=col2)
    table = ColumnSet(columns=[column1,column2])
    card = AdaptiveCard(body=[greeting, table])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":     card.to_dict(),
    }
    print(card.to_json(pretty=True))
    return attachment


def create_new_instanceCard(tags,instanceid):

    greeting = TextBlock(
        f"New EC2 Instance ID: {str(instanceid)}  Has Been Created Please Validate Your Tags",
            size=FontSize.LARGE,horizontalAlignment=HorizontalAlignment.CENTER)
    col= [TextBlock(text="Data Classification"),
          Text(id='DataClassification',
               placeholder=str(tags.dataclassification)),
          TextBlock(text="Environment"),
          Text(id='Environment', placeholder=str(tags.environment)),
          TextBlock(text="ResourceOwner"),
          Text(id='ResourceOwner', placeholder=str(tags.resourceowner)),
          TextBlock(text="Cisco Mail Alias"),
          Text(id='CiscMailAlias', placeholder=str(tags.ciscomailalias)),
          TextBlock(text="Data Taxonomy"),
          Text(id='DataTaxonomy', placeholder=str(tags.datataxonomy)),
          TextBlock(text="Application Name"),
          Text(id='AppName', placeholder=str(tags.appname))]
    column = Column(items=col,verticalContentAlignment=VerticalContentAlignment.CENTER,width="Stretch")
    table = ColumnSet(columns=[column])
    submit = Submit(title="Submit")
    card = AdaptiveCard(body=[greeting,table],actions=[submit])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":card.to_dict(),
    }
    return attachment


def static_new_instance(tags,instanceid):

    greeting = TextBlock(
        f"New EC2 Instance ID: {str(instanceid)}  Has Been Created Please Validate Your Tags",
            size=FontSize.LARGE,horizontalAlignment=HorizontalAlignment.CENTER)
    

    _data_classification = Fact(title="Data Classification",value=str(tags.dataclassification))
    _environment = Fact(title='Environment', value=str(tags.environment))
    _resourc_oewner = Fact(title='ResourceOwner', value=str(tags.resourceowner))
    _cisco_mail_alias = Fact(title="Cisco Mail Alias",value=str(tags.ciscomailalias))
    _data_taxonomy = Fact(title="Data Taxonomy",value=str(tags.data_taxonomy))
    _app_name = Fact(title="Application Name",value=str(tags.AppName))
    info = FactSet(facts=[_data_classification,_environment,_resourc_oewner,_app_name,_data_taxonomy,_app_name])
    approve = Submit(title="Approve", data={"instid": instanceid})
    card = AdaptiveCard(body=[greeting,info],actions=[approve])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":card.to_dict(),
    }
    return attachment




# {device['id']}

