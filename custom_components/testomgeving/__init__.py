DOMAIN = "testomgeving"

async def async_setup(hass, config):
    hass.states.async_set("testomgeving")

    return True
