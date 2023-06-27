__all__ = ("async_setup_entry", "ENTITY_TYPES", "PandoraCASButton")

import asyncio
import logging
from dataclasses import dataclass
from functools import partial
from typing import Optional, Callable, Mapping, Union

from homeassistant.components.button import (
    ButtonEntity,
    ENTITY_ID_FORMAT,
    ButtonEntityDescription,
)
from homeassistant.const import EntityCategory

from custom_components.pandora_cas.api import CommandID, PandoraDeviceTypes
from custom_components.pandora_cas.entity import (
    async_platform_setup_entry,
    PandoraCASEntity,
    PandoraCASEntityDescription,
    CommandType,
    parse_description_command_id,
)

_LOGGER = logging.getLogger(__name__)


@dataclass
class PandoraCASButtonEntityDescription(
    PandoraCASEntityDescription, ButtonEntityDescription
):
    command: Optional[Union[CommandType, Mapping[str, CommandType]]] = None
    icon_pressing: Optional[str] = "mdi:progress-clock"


ENTITY_TYPES = [
    PandoraCASButtonEntityDescription(
        key="erase_errors",
        name="Erase Errors",
        command={
            None: CommandID.ERASE_DTC,
            PandoraDeviceTypes.NAV12: CommandID.NAV12_RESET_ERRORS,
        },
        entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:eraser",
    ),
    PandoraCASButtonEntityDescription(
        key="read_errors",
        name="Read Errors",
        command=CommandID.READ_DTC,
        entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:barcode-scan",
    ),
    PandoraCASButtonEntityDescription(
        key="trigger_horn",
        name="Trigger Horn",
        command=CommandID.TRIGGER_HORN,
        icon="mdi:bugle",
    ),
    PandoraCASButtonEntityDescription(
        key="trigger_light",
        name="Trigger Light",
        command=CommandID.TRIGGER_LIGHT,
        icon="mdi:car-light-high",
    ),
    PandoraCASButtonEntityDescription(
        key="trigger_trunk",
        name="Trigger Trunk",
        command=CommandID.TRIGGER_TRUNK,
        icon="mdi:open-in-app",
    ),
    PandoraCASButtonEntityDescription(
        key="check",
        name="Check",
        command=CommandID.CHECK,
        icon="mdi:refresh",
    ),
    PandoraCASButtonEntityDescription(
        key="additional_command_1",
        name="Additional Command 1",
        command=CommandID.ADDITIONAL_COMMAND_1,
        icon="mdi:numeric-1-box",
    ),
    PandoraCASButtonEntityDescription(
        key="additional_command_2",
        name="Additional Command 2",
        command=CommandID.ADDITIONAL_COMMAND_2,
        icon="mdi:numeric-2-box",
    ),
]


class PandoraCASButton(PandoraCASEntity, ButtonEntity):
    ENTITY_ID_FORMAT = ENTITY_ID_FORMAT
    ENTITY_TYPES = ENTITY_TYPES

    entity_description: PandoraCASButtonEntityDescription

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._is_pressing: bool = False
        self._command_waiter: Optional[Callable[[], ...]] = None
        self._command_press_listener: Optional[Callable[[], ...]] = None

    @property
    def icon(self) -> str | None:
        e = self.entity_description
        if not self.available:
            return e.icon
        if (i := e.icon_pressing) and self._is_pressing:
            return i
        return e.icon

    def press(self) -> None:
        """Compatibility for synchronous turn on calls."""
        asyncio.run_coroutine_threadsafe(
            self.async_press(), self.hass.loop
        ).result()

    def reset_command_event(self, *args) -> None:
        super().reset_command_event(*args)
        self._is_pressing = False

    async def async_press(self) -> None:
        """Proxy method to run disable boolean command."""

        self.reset_command_event()
        self._is_pressing = True
        await self.run_device_command(
            parse_description_command_id(
                self.entity_description.command, self.pandora_device.type
            )
        )

    def update_native_value(self) -> bool:
        """Native value for this entity type does not get updated.

        Therefore, an overriding placeholder is required to
        not do anything at all and not to trigger availability
        issues."""
        return True

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._add_command_listener(self.entity_description.command)


async_setup_entry = partial(
    async_platform_setup_entry,
    PandoraCASButton,
    logger=_LOGGER,
)