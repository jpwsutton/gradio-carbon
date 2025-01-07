"""IBM Carbon theme for gradio demos."""

from __future__ import annotations

import gradio as gr
from gradio.themes.base import Base

DEFAULT_PRIMARY_HUE = gr.themes.Color(
    c100="#D0E2FF",
    c200="#A6C8FF",
    c300="#78A9FF",
    c400="#4589FF",
    c50="#EDF5FF",
    c500="#0F62FE",
    c600="#0043CE",
    c700="#002D9C",
    c800="#001D6C",
    c900="#001141",
    c950="#001141",
)

DEFAULT_SECONDARY_HUE = gr.themes.Color(
    c100="#D0E2FF",
    c200="#A6C8FF",
    c300="#4589FF",
    c400="#4589FF",
    c50="#EDF5FF",
    c500="#0F62FE",
    c600="#0043CE",
    c700="#002D9C",
    c800="#001D6C",
    c900="#001141",
    c950="#001141",
)

DEFAULT_NEUTRAL_HUE = gr.themes.Color(
    c100="#DDE1E6",
    c200="#C1C7CD",
    c300="#A2A9B0",
    c400="#878D96",
    c50="#F2F4F8",
    c500="#697077",
    c600="#4D5358",
    c700="#343A3F",
    c800="#21272A",
    c900="#121619",
    c950="#121619",
)

DEFAULT_TEXT_SIZE = gr.themes.Size(lg="16px", md="14px", sm="14px", xl="20px", xs="14px", xxl="28px", xxs="12px")
DEFAULT_SPACING_SIZE = gr.themes.Size(lg="8px", md="8px", sm="4px", xl="16px", xs="4px", xxl="16px", xxs="2px")
DEFAULT_RADIUS_SIZE = gr.themes.Size(lg="8px", md="8px", sm="4px", xl="12px", xs="2px", xxl="22px", xxs="1px")

DEFAULT_FONTS = ["IBM Plex Sans", "IBM Plex Sans", "IBM Plex Sans", "IBM Plex Sans"]
DEFAULT_MONO_FONTS = ["IBM Plex Mono", "IBM Plex Mono", "IBM Plex Mono", "IBM Plex Mono"]


class Carbon(Base):
    """Base Carbon Theme Class."""

    def __init__(
        self,
        *,
        primary_hue: gr.themes.Color = DEFAULT_PRIMARY_HUE,
        secondary_hue: gr.themes.Color = DEFAULT_SECONDARY_HUE,
        neutral_hue: gr.themes.Color = DEFAULT_NEUTRAL_HUE,
        text_size: gr.themes.Size = DEFAULT_TEXT_SIZE,
        spacing_size: gr.themes.Size = DEFAULT_SPACING_SIZE,
        radius_size: gr.themes.Size = DEFAULT_RADIUS_SIZE,
        font: list[str] = DEFAULT_FONTS,
        font_mono: list[str] = DEFAULT_MONO_FONTS,
    ) -> None:
        """Initialise Theme Class."""
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = "carbon"
        super().set(
            body_text_color="*neutral_950",
            body_text_color_dark="*neutral_50",
            body_text_size="*text_lg",
            body_text_color_subdued="*neutral_300",
            body_text_color_subdued_dark="*neutral_500",
            body_text_weight="300",
            embed_radius="*radius_md",
            background_fill_secondary="*background_fill_primary",
            background_fill_secondary_dark="*neutral_950",
            border_color_accent="*neutral_100",
            border_color_accent_dark="*neutral_800",
            border_color_accent_subdued="*neutral_100",
            border_color_accent_subdued_dark="*neutral_800",
            border_color_primary="*neutral_300",
            border_color_primary_dark="*neutral_800",
            shadow_drop="*block_label_shadow",
            shadow_drop_lg="0px 1px 2px 0px rgba(0, 0, 0, 0.07)",
            shadow_inset="0px 2px 4px 0px rgba(0, 0, 0, 0.07) inset, 0px 0px 3px 0px rgba(0, 0, 0, 0.00) inset",
            shadow_spread="1px",
            chatbot_text_size="*text_xs",
            checkbox_background_color_hover="*neutral_50",
            checkbox_background_color_hover_dark="*neutral_50",
            checkbox_background_color_selected="*neutral_800",
            checkbox_background_color_selected_dark="*neutral_800",
            checkbox_border_color_selected="*neutral_950",
            checkbox_border_color_selected_dark="*neutral_950",
            checkbox_label_border_width="1px",
            checkbox_label_border_width_dark="1px",
            checkbox_label_padding="*spacing_xs",
            checkbox_label_text_size="*text_xs",
            input_background_fill="*background_fill_primary",
            input_border_color_focus="*primary_500",
            input_border_width="1px",
            input_border_width_dark="1px",
            input_padding="*spacing_lg",
            input_text_size="*text_xs",
            button_large_padding="*spacing_sm",
            button_small_padding="*spacing_xxs",
            button_primary_border_color_dark="*primary_700",
            button_primary_border_color_hover_dark="*primary_700",
            button_primary_shadow="*shadow_drop",
            button_primary_shadow_hover="*shadow_drop_lg",
            button_secondary_background_fill="*neutral_100",
            button_secondary_background_fill_hover="*neutral_200",
            button_secondary_border_color="*neutral_100",
            button_secondary_border_color_hover_dark="*neutral_700",
            button_secondary_shadow_hover="*shadow_drop_lg",
        )
