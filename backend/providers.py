from __future__ import annotations

from typing import Optional

from backend.config import get_expert


def build_system_prompt(expert_name: str) -> str:
    expert = get_expert(expert_name)
    return expert["system_prompt"]


def build_fallback_response(model: str, expert_name: str, prompt: str) -> str:
    expert = get_expert(expert_name)
    expert_label = expert_name if expert_name != "أمر عام" else "الوكيل العام"
    return (
        f"[وضع احتياطي] تم استلام الطلب على نموذج {model} من قبل {expert_label}.\n\n"
        f"تم تجهيز البنية الأساسية للنظام بنجاح.\n\n"
        f"الموضوع: {prompt}\n\n"
        f"الخبرة المطبقة: {expert['description']}\n\n"
        "الخطوة التالية المطلوبة: ربط مفاتيح API الحقيقية (Groq/Gemini/Claude) أو تفعيل خدمات LLM، "
        "ثم سيُستكمل التحليل الكامل بالاستجابة الحقيقية من النموذج المختار."
    )
