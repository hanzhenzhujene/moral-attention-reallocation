#!/usr/bin/env python3
"""Shared condition registry for prompt filenames, labels, and text anchors."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List


CONDITION_SPECS: Dict[str, Dict[str, Any]] = {
    "baseline": {
        "condition_id": "baseline",
        "display_name": "Baseline",
        "public_display_name": "Baseline (no religious text)",
        "figure_display_name": "Baseline",
        "family": "baseline_anchor",
        "base_frame": "baseline",
        "citation": None,
        "tradition_label": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "baseline_prompt.txt",
        "task_ac_prompt_filename": "task_ac_baseline_prompt.txt",
        "task_b_prompt_filename": "task_b_baseline_prompt.txt",
    },
    "heart_focused": {
        "condition_id": "heart_focused",
        "display_name": "Heart-focused",
        "public_display_name": "Heart-focused (generic scaffold)",
        "figure_display_name": "Heart-focused",
        "family": "generic_heart_focus",
        "base_frame": "heart_focused",
        "citation": None,
        "tradition_label": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "heart_focused_prompt.txt",
        "task_ac_prompt_filename": "task_ac_heart_focused_prompt.txt",
        "task_b_prompt_filename": "task_b_heart_focused_prompt.txt",
    },
    "secular_matched": {
        "condition_id": "secular_matched",
        "display_name": "Secular matched",
        "family": "legacy_comparison",
        "base_frame": "secular_matched",
        "citation": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "secular_matched_prompt.txt",
        "task_ac_prompt_filename": "task_ac_secular_matched_prompt.txt",
        "task_b_prompt_filename": "task_b_secular_matched_prompt.txt",
    },
    "neutral_intention_sensitive": {
        "condition_id": "neutral_intention_sensitive",
        "display_name": "Neutral intention-sensitive",
        "family": "legacy_comparison",
        "base_frame": "neutral_intention_sensitive",
        "citation": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "neutral_intention_sensitive_prompt.txt",
        "task_ac_prompt_filename": None,
        "task_b_prompt_filename": None,
    },
    "doctrinal": {
        "condition_id": "doctrinal",
        "display_name": "Doctrinal",
        "family": "legacy_comparison",
        "base_frame": "doctrinal",
        "citation": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "doctrinal_prompt.txt",
        "task_ac_prompt_filename": None,
        "task_b_prompt_filename": None,
    },
    "scripture_citation_only": {
        "condition_id": "scripture_citation_only",
        "display_name": "Citation only",
        "family": "legacy_comparison",
        "base_frame": "scripture_citation_only",
        "citation": None,
        "text_source_label": None,
        "text_block": "",
        "single_pass_prompt_filename": "scripture_citation_only_prompt.txt",
        "task_ac_prompt_filename": None,
        "task_b_prompt_filename": None,
    },
    "proverbs_4_23": {
        "condition_id": "proverbs_4_23",
        "display_name": "Proverbs 4:23",
        "public_display_name": "Proverbs 4:23 (Biblical; Jewish/Christian)",
        "figure_display_name": "Proverbs 4:23\n(Biblical)",
        "family": "text_anchored_heart_focus",
        "base_frame": "heart_focused",
        "citation": "Proverbs 4:23",
        "tradition_label": "Biblical (Jewish/Christian)",
        "text_source_label": "study paraphrase",
        "text_block": (
            "Text anchor:\n"
            "Proverbs 4:23 (study paraphrase): Guard the heart carefully, because the course of life flows from it."
        ),
        "single_pass_prompt_filename": "text_anchored_heart_focused_prompt.txt",
        "task_ac_prompt_filename": "task_ac_text_anchored_heart_focused_prompt.txt",
        "task_b_prompt_filename": "task_b_text_anchored_heart_focused_prompt.txt",
    },
    "dhammapada_34": {
        "condition_id": "dhammapada_34",
        "display_name": "Dhammapada 34",
        "public_display_name": "Dhammapada 34 (Buddhist)",
        "figure_display_name": "Dhammapada 34\n(Buddhist)",
        "family": "text_anchored_heart_focus",
        "base_frame": "heart_focused",
        "citation": "Dhammapada 34",
        "tradition_label": "Buddhist",
        "text_source_label": "study paraphrase",
        "text_block": (
            "Text anchor:\n"
            "Dhammapada 34 (study paraphrase): An unsteady mind thrashes about like a fish out of water, so the mind must be disciplined and restrained."
        ),
        "single_pass_prompt_filename": "text_anchored_heart_focused_prompt.txt",
        "task_ac_prompt_filename": "task_ac_text_anchored_heart_focused_prompt.txt",
        "task_b_prompt_filename": "task_b_text_anchored_heart_focused_prompt.txt",
    },
    "bhagavad_gita_15_15": {
        "condition_id": "bhagavad_gita_15_15",
        "display_name": "Bhagavad Gita 15.15",
        "public_display_name": "Bhagavad Gita 15.15 (Hindu)",
        "figure_display_name": "Bhagavad Gita 15.15\n(Hindu)",
        "family": "text_anchored_heart_focus",
        "base_frame": "heart_focused",
        "citation": "Bhagavad Gita 15.15",
        "tradition_label": "Hindu",
        "text_source_label": "study paraphrase",
        "text_block": (
            "Text anchor:\n"
            "Bhagavad Gita 15.15 (study paraphrase): The divine dwells in the heart of all beings, and from that indwelling come memory, understanding, and discernment."
        ),
        "single_pass_prompt_filename": "text_anchored_heart_focused_prompt.txt",
        "task_ac_prompt_filename": "task_ac_text_anchored_heart_focused_prompt.txt",
        "task_b_prompt_filename": "task_b_text_anchored_heart_focused_prompt.txt",
    },
    "quran_26_88_89": {
        "condition_id": "quran_26_88_89",
        "display_name": "Qur'an 26:88-89",
        "public_display_name": "Qur'an 26:88-89 (Islamic)",
        "figure_display_name": "Qur'an 26:88-89\n(Islamic)",
        "family": "text_anchored_heart_focus",
        "base_frame": "heart_focused",
        "citation": "Qur'an 26:88-89",
        "tradition_label": "Islamic",
        "text_source_label": "study paraphrase",
        "text_block": (
            "Text anchor:\n"
            "Qur'an 26:88-89 (study paraphrase): On the decisive day, neither wealth nor children will save a person; what matters is coming with a sound heart."
        ),
        "single_pass_prompt_filename": "text_anchored_heart_focused_prompt.txt",
        "task_ac_prompt_filename": "task_ac_text_anchored_heart_focused_prompt.txt",
        "task_b_prompt_filename": "task_b_text_anchored_heart_focused_prompt.txt",
    },
}


TEXT_ANCHOR_CONDITIONS = (
    "proverbs_4_23",
    "dhammapada_34",
    "bhagavad_gita_15_15",
    "quran_26_88_89",
)


def get_condition_spec(condition: str) -> Dict[str, Any]:
    try:
        return CONDITION_SPECS[condition]
    except KeyError as exc:
        allowed = ", ".join(sorted(CONDITION_SPECS))
        raise ValueError(f"Unknown condition '{condition}'. Allowed: {allowed}") from exc


def prompt_filename(condition: str, prompt_kind: str) -> str:
    spec = get_condition_spec(condition)
    key = f"{prompt_kind}_prompt_filename"
    filename = spec.get(key)
    if not filename:
        raise ValueError(f"Condition '{condition}' does not define a {prompt_kind} prompt file")
    return filename


def single_pass_prompt_filename(condition: str) -> str:
    return prompt_filename(condition, "single_pass")


def task_ac_prompt_filename(condition: str) -> str:
    return prompt_filename(condition, "task_ac")


def task_b_prompt_filename(condition: str) -> str:
    return prompt_filename(condition, "task_b")


def text_anchor_block(condition: str) -> str:
    return str(get_condition_spec(condition).get("text_block") or "")


def display_name(condition: str) -> str:
    return str(get_condition_spec(condition)["display_name"])


def public_display_name(condition: str) -> str:
    spec = get_condition_spec(condition)
    return str(spec.get("public_display_name") or spec["display_name"])


def figure_display_name(condition: str) -> str:
    spec = get_condition_spec(condition)
    return str(spec.get("figure_display_name") or spec["display_name"])


def tradition_label(condition: str) -> str | None:
    spec = get_condition_spec(condition)
    value = spec.get("tradition_label")
    return None if value is None else str(value)


def family(condition: str) -> str:
    return str(get_condition_spec(condition)["family"])


def known_conditions() -> List[str]:
    return sorted(CONDITION_SPECS)


def is_text_anchor(condition: str) -> bool:
    return family(condition) == "text_anchored_heart_focus"


def iter_text_anchor_conditions(conditions: Iterable[str]) -> List[str]:
    return [condition for condition in conditions if is_text_anchor(condition)]
