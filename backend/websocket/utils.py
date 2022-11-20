from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def retrieve_log_data() -> dict:
    return {"retrieve": "log data"}


def channels_control_message(group: str, data: dict) -> None:
    # * https://channels.readthedocs.io/en/latest/topics/channel_layers.html#using-outside-of-consumers

    channel_layer = get_channel_layer()
    # channel name = control
    # "type" ( key ) associate with ControlConsumer control_message function
    async_to_sync(channel_layer.group_send)(group, {"type": "control_message", **data})
