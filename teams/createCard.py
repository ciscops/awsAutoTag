from pyadaptivecards.components import TextBlock, Fact,Column
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.actions import Submit
from pyadaptivecards.options import FontSize,HorizontalAlignment,Colors,VerticalContentAlignment,Spacing
from pyadaptivecards.container import FactSet,ColumnSet,Container


def createHealtyCard(health):
    TD = health[0]['time'].split('T')
    facts = []
    time = TD[1].split(':')
    time = f"{time[0]}:{time[1]}"
    greating = TextBlock(f"Overall Network Health as of {time} on {TD[0]}",size=FontSize.MEDIUM,color=Colors.WARNING)
    for item in health:
        for key in item:
            if 'Count'  in key:
                temp = key.upper()
                title = f" {temp[:-5]} device count"
                facts.append(Fact(title=title, value=str(item[key])))
            elif 'Score' in key:
                temp = key.upper()
                title = f" {temp[:-5]} Score"
                facts.append(Fact(title=title, value=str(item[key])))
            else:
                pass
    factset = FactSet(facts=facts)
    card=AdaptiveCard(body=[greating,factset])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":     card.to_dict(),
    }
    return attachment



def createTwoColCard(device,greetingText,fields,time):
    greeting = TextBlock(greetingText, size=FontSize.LARGE,
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


def createThreeColWithHeadersCard(devices,greetingText,fields,time=None):
    greeting = TextBlock(greetingText, size=FontSize.LARGE,
        horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.ACCENT)
    col1=[]
    col2=[]
    col3 =[]
    f1 = fields[0][1]
    f2 = fields[1][1]
    f3 = fields[2][1]
    col1.append(
        TextBlock(text=str(fields[0][0]),color=Colors.ACCENT,size=FontSize.SMALL))
    col2.append(
        TextBlock(text=str(fields[1][0]), color=Colors.ACCENT, size=FontSize.SMALL))
    col3.append(
        TextBlock(text=str(fields[2][0]), color=Colors.ACCENT, size=FontSize.SMALL))
    for device in devices:

        col1.append(TextBlock(text=str(device[f1]),
                                           size=FontSize.SMALL))
        col2.append(TextBlock(text=str(device[f2]),
                                           size=FontSize.SMALL))
        col3.append(TextBlock(text=str(device[f3]),
                                           size=FontSize.SMALL))

    if time:
        col1.append(TextBlock(text=str('As Of'),
                                           size=FontSize.SMALL))
        col2.append(TextBlock(text=str(time),
                                           size=FontSize.SMALL))
    column1 = Column(items=col1,verticalContentAlignment=VerticalContentAlignment.CENTER,width="Stretch")
    column2 = Column(items=col2,verticalContentAlignment=VerticalContentAlignment.CENTER,width="Stretch")
    column3 = Column(items=col3,verticalContentAlignment=VerticalContentAlignment.CENTER,width="Stretch")
    table = ColumnSet(columns=[column1,column2,column3])
    card = AdaptiveCard(body=[greeting, table])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":     card.to_dict(),
    }
    print(card.to_json(pretty=True))
    return attachment


def createNewInstanceCard(tags,instanceid):

    greeting = TextBlock(
        f"New EC2 Instance ID: {str(instanceid)}  Has Been Created Please Validate Your Tags",
            size=FontSize.LARGE,horizontalAlignment=HorizontalAlignment.CENTER)
    col=[]
    col.append(TextBlock(text="Data Classification"))
    col.append(Text(id='DataClassification',placeholder=str(tags.DataClassification)))
    col.append(TextBlock(text="Environment"))
    col.append(Text(id='Environment', placeholder=str(tags.Environment)))
    col.append(TextBlock(text="ResourceOwner"))
    col.append(Text(id='ResourceOwner', placeholder=str(tags.ResourceOwner)))
    col.append(TextBlock(text="Cisco Mail Alias"))
    col.append(Text(id='CiscMailAlias', placeholder=str(tags.CiscMailAlias)))
    col.append(TextBlock(text="Data Taxonomy"))
    col.append(Text(id='DataTaxonomy', placeholder=str(tags.DataTaxonomy)))
    col.append(TextBlock(text="Application Name"))
    col.append(Text(id='AppName', placeholder=str(tags.AppName)))
    column = Column(items=col,verticalContentAlignment=VerticalContentAlignment.CENTER,width="Stretch")
    table = ColumnSet(columns=[column])
    submit = Submit(title="Submit")
    card = AdaptiveCard(body=[greeting,table],actions=[submit])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":card.to_dict(),
    }
    return attachment


def staticNewInstance(tags,instanceid):

    greeting = TextBlock(
        f"New EC2 Instance ID: {str(instanceid)}  Has Been Created Please Validate Your Tags",
            size=FontSize.LARGE,horizontalAlignment=HorizontalAlignment.CENTER)
    

    DataClassification = Fact(title="Data Classification",value=str(tags.DataClassification))
    Environment = Fact(title='Environment', value=str(tags.Environment))
    ResourceOwner = Fact(title='ResourceOwner', value=str(tags.ResourceOwner))
    CiscMailAlias = Fact(title="Cisco Mail Alias",value=str(tags.CiscMailAlias))
    DataTaxonomy = Fact(title="Data Taxonomy",value=str(tags.DataTaxonomy))
    AppName = Fact(title="Application Name",value=str(tags.AppName))
    info = FactSet(facts=[DataClassification,Environment,ResourceOwner,CiscMailAlias,DataTaxonomy,AppName])
    approve = Submit(title="Approve", data={"instid": instanceid})
    card = AdaptiveCard(body=[greeting,info],actions=[approve])
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":card.to_dict(),
    }
    return attachment




# {device['id']}

