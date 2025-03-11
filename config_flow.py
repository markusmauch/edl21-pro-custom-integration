"""Config flow for EDL21 integration."""

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import CONF_SERIAL_PORT, CONF_UPDATE_INTERVAL, DEFAULT_TITLE, DOMAIN

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_SERIAL_PORT): str,
        vol.Required(CONF_UPDATE_INTERVAL, default=60): int,
    }
)


class EDL21ConfigFlow(ConfigFlow, domain=DOMAIN):
    """EDL21 config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, str] | None = None
    ) -> ConfigFlowResult:
        """Handle the user setup step."""
        if user_input is not None:
            self._async_abort_entries_match(
                {
                    CONF_SERIAL_PORT: user_input[CONF_SERIAL_PORT],
                    CONF_UPDATE_INTERVAL: user_input[CONF_UPDATE_INTERVAL],
                }
            )

            return self.async_create_entry(
                title=DEFAULT_TITLE,
                data=user_input,
            )

        data_schema = self.add_suggested_values_to_schema(DATA_SCHEMA, user_input)
        return self.async_show_form(step_id="user", data_schema=data_schema)
