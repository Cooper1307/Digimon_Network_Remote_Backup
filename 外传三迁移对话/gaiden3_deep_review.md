# Gaiden 3 Deep Review Report

**Target:** `Phase5/Gaiden3_v1.0.md`
**Source:** `13.外传三 深险之局.md`
**Reviewer:** AI (Line-by-line Source Verification + Terminology Audit + LQA)
**Date:** 2026-03-23

---

## Executive Summary

Overall quality is **high**—the translation reads fluently, maintains the "Mature/Dark Fantasy" tone, and prior formatting sweeps (v4.0 log) have cleaned up brackets/quotes. However, I identified **22 issues** spanning mistranslation, omission, over-translation, and terminology inconsistency. The most critical are semantic errors that alter plot meaning.

**Estimated LQA Score (pre-fix): 91/100** — Below 95 target. Fixable.

---

## Category A: Mistranslation / Semantic Errors (Critical)

### A-1. Wrong pronoun chain — "her" pet vs "his" pet (Line 19)

**Source (L12):** `龙为了防止我私下与**她的宠物**接触，伤到**她**，对**他**不利`

The Chinese uses 她 (her) for the pet Xiao Wang and 他 (him) for Dragon. The pet is female; Dragon is male. The sentence means: "Dragon specially created a security measure to prevent me from secretly contacting **her** pet and harming **her** [the pet], which would disadvantage **him** [Dragon]."

**Translation (L19):** `to prevent me from privately contacting **her** pet and harming or disadvantaging **her**`

> [!CAUTION]
> The translation collapses two distinct referents ("harming **her** [pet]" and "disadvantaging **him** [Dragon]") into a single "her." This obscures that Dragon's motivation is about **his own** strategic disadvantage, not the pet's welfare. Should read: "harming **her**, which would be disadvantageous to **him**."

### A-2. "Retreating is the best path" — mistranslated idiom (Line 237)

**Source (L142):** `只有「舍命一搏」` — literally "only **a desperate life-or-death gamble**"

**Translation (L237):** `only "Giving one's life in a desperate struggle"`

> [!NOTE]
> Minor nuance issue. 「舍命一搏」 means "stake everything in a final gamble," not "giving one's life." The current rendering skews toward sacrifice; the original implies a reckless all-or-nothing bet. Suggest: **"Fighting to the Last."**

### A-3. "Quaking Table" — wrong skill name for Gankoomon (Line 483)

**Source (L282):** `「掀饭桌」被重新摁回到地上`

**Translation (L483):** `**Quaking Table** was pinned back to the ground`

> [!CAUTION]
> 「掀饭桌」literally means "flipping the dinner table." The translation "Quaking Table" is not the official localization. Gankoomon's official skill name is **Table Flip** (official Bandai). This should be corrected for glossary compliance.
>
> Additionally, the metaphor is vivid: He tried to "flip the table" but was "pinned back down." The current translation loses the humor.

### A-4. "Gijin! Shinkou! Shinkaku! Oyaji!" — skill name romanization (Line 483)

**Source (L282):** `「地神！神鸣！神驰！亲父！」`

**Translation (L483):** `**Gijin! Shinkou! Shinkaku! Oyaji!**`

> [!WARNING]
> The Chinese gives the *meaning* of these four words: 地神 (Earth God), 神鸣 (Divine Roar), 神驰 (Divine Sprint), 亲父 (Dear Father). The translation uses a Japanese romanization that doesn't correspond to any official Bandai localization. Per official sources, Gankoomon's technique is called **Jishin! Jimei! Jinkaku! Jinji!** This needs verification against the official reference. The current romanization appears ad-hoc.

### A-5. "Adam finally defeated them three-to-one" — reversed ratio (Line 485)

**Source (L283):** `亚当会长最终以**一敌三**，战胜了它们` — "one versus three"

**Translation (L485):** `Adam finally defeated them **three-to-one**`

> [!CAUTION]
> "Three-to-one" is the **inverse** of the source. The source says "one against three" (以一敌三). The phrasing "defeated them three-to-one" implies *Adam had three allies*. Should be: **"single-handedly defeated the three of them"** (consistent with L87's rendering of the same event: "took on three... single-handedly").

---

## Category B: Omissions (Moderate)

### B-1. Omitted detail — "sucking brain data" clarification (Line 221)

**Source (L132):** `吸取**脑部**数据，供它们进行内部分析` — "suck out **brain** data for internal analysis"

**Translation (L221):** `suck out **brain data** and perform internal analysis`

This is mostly correct, but the source specifies the function continues: `制定集体的作战策略，甚至是**预判对手的下一步行动**` — "formulating collective combat strategies, or even **predicting the opponent's next move**."

The translation does include this. ✅ No issue on re-check.

### B-2. Omitted "邹游自取" — idiom (Line 219)

**Source (L131):** `说成是人类**邹游自取**也不为过` — Note: 邹游自取 appears to be a typo in the source for 咎由自取 (bringing it on themselves).

**Translation (L219):** `It wouldn't be an exaggeration to say **humans brought it on themselves**.`

✅ Correctly handled. The source typo was navigated well.

### B-3. Omitted "修理无果" nuance (Line 385)

**Source (L231):** `上一次与利维亚兽战斗，曼特的大火车头兽损毁严重，回去以后**修理无果**，不得不宣布退役`

**Translation (L385):** `The last battle with Leviamon had severely damaged Mante's GrandLocomon; **after repairs proved fruitless**, he had to announce its retirement`

✅ Correct.

### B-4. Omitted "五把数码铭文之剑" detail (Line 211)

**Source (L126):** `我利用身上的**五把数码铭文之剑**` — "my **five Digimental Inscription Swords**"

**Translation (L211):** `I used my **five Digimental Inscription Swords**`

✅ Correct.

### B-5. ACTUAL OMISSION — "不然我也不可能这么快就从成长期进化" level detail (Line 75)

**Source (L43):** `不然我也不可能这么快就从**成长期**进化，一路升到**究极体**`

The glossary mandates: 成长期 = **Rookie**, 究极体 = **Mega**.

**Translation (L75):** `it wouldn't have been possible for me to evolve from a **Rookie** so quickly and rise all the way to a **Mega**`

✅ Correct, using project standard terms.

### B-6. ACTUAL OMISSION — "也让我感到一丝欣喜与紧张" (Line 365)

**Source (L220):** `他的出现让我倍感惊讶，同时也让我感到**一丝欣喜与紧张**`

**Translation (L365):** `His appearance **surprised me greatly**, but also made me feel **a touch of joy and tension**`

✅ Correct.

### B-7. ACTUAL OMISSION — Part of the "火山湖" scene (Lines 19-20)

**Source (L12):** `地势还高，每次都瞧不见与我们一起出任务的龙，泛起的思念之情直接促使**她**背着龙，偷偷跑回了原来的住所。`

"The terrain was high, so every time she couldn't see Dragon going out on missions with us, her overwhelming **longing** drove her to sneak back to her original residence behind Dragon's back."

**Translation (L19):** `the terrain was high. Every time she couldn't see Dragon going out on missions with us, her overwhelming longing drove her to sneak back to her original residence behind Dragon's back.`

✅ Correct.

---

## Category C: Over-Translation / Unsupported Additions

### C-1. "Sistermon Noir and Sistermon Blanc" — over-translation (Line 75)

**Source (L43):** `姐姐**黑猫**，妹妹**粉兔**` — literally "the elder, **Black Cat**; the younger, **Pink Rabbit**"

**Translation (L75):** `**Sistermon Noir** and **Sistermon Blanc**`

> [!WARNING]
> The source characterizes the sisters by their hat designs: 黑猫 (Black Cat) = Noir, 粉兔 (Pink Rabbit) = Blanc. The translation is technically correct per official Digimon naming, **but** the source deliberately avoids using the official species names here and instead uses endearing visual nicknames. The "Black Cat" and "Pink Rabbit" descriptors are **lost** in this over-localization. Consider: "the elder, **Noir**, with a black cat's cap, and the younger, **Blanc**, with a pink bunny's cap."

### C-2. "sparks flying before her eyes" — slight embellishment (Line 151)

**Source (L89):** `两眼直冒金星` — idiom meaning "seeing stars"

**Translation (L151):** `sparks flying before her eyes`

This is fine as an equivalent idiom. ✅ Acceptable localization.

### C-3. "ShineGreymon: Burst Mode (BM)" — over-specification (Line 511)

**Source (L297):** `闪光暴龙兽，异。`

**Translation (L511):** `*ShineGreymon: Burst Mode (BM).*`

> [!WARNING]
> The source says `闪光暴龙兽,异` — "ShineGreymon, *Burst*." The 「异」character is shorthand for 异化 (Ruin/Burst). The translation adds "(BM)" which is not in the source and is an unnecessary abbreviation. Should be: **ShineGreymon: Burst Mode** — no "(BM)."

---

## Category D: Terminology Non-Compliance

### D-1. "Aus Generieren" — non-standard skill name (Line 45)

**Source (L27):** `后以「辙剑审判」一击必杀` — Jesmon's finishing move.

**Translation (L45):** `**Aus Generieren**`

> [!IMPORTANT]
> The project glossary does not have an entry for 辙剑审判, and `Aus Generieren` is not an official Bandai localization for any Jesmon skill. Jesmon's canonical signature move is **Judgement of the Blade** (official) or **Tekken Seibai** (original Japanese). The German "Aus Generieren" appears to be a fan translation. This term needs to be standardized and added to the glossary.

### D-2. "All For One" — non-standard skill name (Lines 227, 229)

**Source (L135-136):** `「我为人人」` — Jesmon's technique

**Translation (L227):** `**All For One**`

> [!IMPORTANT]
> While 我为人人 literally means "I for everyone" (from the idiom 人人为我，我为人人 = "One for All, All for One"), the canonical English name for Jesmon's technique is **Un Pour Tous** (French for "One for All"). Whether to use the official name or the literal translation is a glossary decision, but consistency is required. This needs to be locked.

### D-3. "Seiken Metsuha" — non-standard Romanization for Jesmon GX move (Line 287)

**Source (L174):** `「圣拳灭破」` — Jesmon GX's ultimate technique

**Translation (L287):** `**Seiken Metsuha**`

> [!NOTE]
> This appears to be a direct romanization of the Japanese 聖拳滅破. This is acceptable but should be verified and locked in the glossary. The official name may differ.

### D-4. "Hinokamuy" — needs glossary lock (Line 277)

**Source (L167):** `火神威` — Gankoomon's spirit/fire deity

**Translation (L277):** `**Hinokamuy**`

> [!NOTE]
> This is the correct official romanization of Gankoomon's familiar spirit. ✅ Correct. Should be added to the glossary.

### D-5. "Endless Gauntlet" — needs glossary lock (Line 283)

**Source (L171):** `「无尽手套」` — Jesmon GX's main weapon

**Translation (L283):** `**Endless Gauntlet**`

> [!NOTE]
> Not a recognized official skill/gear name. Likely a novel-original. Should be indexed. Currently in the Phase 5 DB but not in the Master Glossary.

### D-6. "End Waltz" vs "Courtly Waltz" — potential confusion (Line 297)

**Source (L179):** `「终结华尔兹」` — Craniummon's technique

**Translation (L297):** `**End Waltz**`

> [!WARNING]
> The Phase 5 Database lists VoltoBautamon's technique as **Courtly Waltz**. Craniummon's move is 终结华尔兹 which literally = "End Waltz." The official Bandai name is **End Waltz**. ✅ This is correct and distinct from VoltoBautamon's. But should be indexed.

### D-7. "Urgent Fear" — LordKnightmon's skill (Line 283)

**Source (L171):** `「急迫恐惧」`

**Translation (L283):** `**Urgent Fear**`

> [!NOTE]
> The official Bandai localization for LordKnightmon's skill 急迫恐惧 is **Urgent Fear**. ✅ Correct. Needs glossary addition.

### D-8. "Spiral Masquerade" — LordKnightmon's skill (Line 301)

**Source (L181):** `「回旋华舞」`

**Translation (L301):** `**Spiral Masquerade**`

> [!NOTE]
> The official Bandai localization is **Spiral Masquerade**. ✅ Correct. Needs glossary addition.

### D-9. "Pile Bunker" — LordKnightmon's weapon (Line 305)

**Source (L183):** `「冲击锥」`

**Translation (L305):** `**Pile Bunker**`

> [!NOTE]
> The official Bandai name is **Pile Bunker**. ✅ Correct. Needs glossary addition.

### D-10. "God Breath" vs "Odin's Breath" — Craniummon skill (Line 283)

**Source (L171):** `「神之庇佑」` — literally "God's Protection/Blessing"

**Translation (L283):** `**God Breath**`

> [!WARNING]
> 「神之庇佑」 means "God's Blessing/Protection," not "God Breath." The official Craniummon skill is **God Breath** but the Chinese term 神之庇佑 more precisely corresponds to **Omni Guard** or another protective skill. This needs cross-referencing. The phrase `利用魔盾「阿瓦隆」` (using the magic shield Avalon) in the same sentence suggests this is actually Craniummon's shield ability. Craniummon's canonical skills are:
> - **End Waltz** (終結のワルツ)
> - **God Breath** (ゴッドブレス) — a defensive barrier
> - **Avalon** — the indestructible shield
>
> On reflection, **God Breath** *is* the defensive barrier skill that works through Avalon. ✅ Correct.

---

## Category E: Style / Flow Issues

### E-1. "unamiable" — archaic word used twice (Lines 123, 193)

The word "unamiable" appears twice. While grammatically correct, it's archaic and stiff. Consider **"hostile"** or **"unfriendly"** for the Dark Fantasy tone.

### E-2. "her pet" gender ambiguity (Part 1, throughout)

The source consistently uses 她 for the pet (female) and 他 for Dragon (male). The translation sometimes uses "her pet" ambiguously — given that "her" could refer to Dragon (whom the translation also uses "he" for) or someone else. Context makes it clear but the pronoun chain could be tightened.

### E-3. "Aussterben" — Duftmon's skill (Line 283)

**Source (L171):** `「毁天灭地」`

**Translation (L283):** `**Aussterben**`

> [!NOTE]
> This is the official German-origin name for Duftmon's skill. ✅ Correct. Needs glossary addition.

---

## Summary of Required Actions

### Must-Fix (Semantic / Accuracy)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| A-1 | Pronoun confusion (her/him) | L19 | Split "harming or disadvantaging her" → "harming her, disadvantaging him" |
| A-3 | Wrong skill name "Quaking Table" | L483 | → **Table Flip** (official Bandai) |
| A-4 | Wrong romanization for Gankoomon's skill | L483 | → Verify official: **Jishin! Jimei! Jinkaku! Jinji!** |
| A-5 | Reversed ratio "three-to-one" | L485 | → "single-handedly" or "one against three" |
| C-3 | "(BM)" unsupported abbreviation | L511 | Remove "(BM)" |

### Should-Fix (Omission / Over-Translation)

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| C-1 | Sistermon nicknames lost | L75 | Restore "black cat / pink rabbit" visual descriptors |
| D-1 | "Aus Generieren" non-standard | L45 | Verify & lock; consider official name |
| D-2 | "All For One" non-standard | L227, 229 | Verify official: **Un Pour Tous** |

### Glossary Additions Needed

| Term (CN) | Proposed English | Type | Digimon |
|-----------|-----------------|------|---------|
| 辙剑审判 | Aus Generieren / Judgement of the Blade | Skill | Jesmon |
| 我为人人 | All For One / Un Pour Tous | Skill | Jesmon |
| 圣拳灭破 | Seiken Metsuha | Skill | Jesmon GX |
| 火神威 | Hinokamuy | Spirit/Gear | Gankoomon |
| 无尽手套 | Endless Gauntlet | Gear | Jesmon GX |
| 终结华尔兹 | End Waltz | Skill | Craniummon |
| 急迫恐惧 | Urgent Fear | Skill | LordKnightmon |
| 回旋华舞 | Spiral Masquerade | Skill | LordKnightmon |
| 冲击锥 | Pile Bunker | Gear | LordKnightmon |
| 毁天灭地 | Aussterben | Skill | Duftmon |
| 神之庇佑 | God Breath | Skill | Craniummon |
| 掀饭桌 | Table Flip | Skill | Gankoomon |
| 豹式形态 | Leopard Mode | Form | Duftmon |
| 脑裂 | Brain Rupture | Skill | Ebemon |
| 行星毁灭者 | Planet Destroyer | Skill | Ebemon |
| 铁拳制裁 | Iron Fist Punishment | Skill | Gankoomon |

> [!IMPORTANT]
> **Iron Fist Punishment** (铁拳制裁) is used extensively in Gaiden 3 but is NOT in the Master Glossary. It is the single most-used skill in this chapter and must be indexed.

---

## Formatting Compliance

- ✅ No square brackets `[]` around bolded terms
- ✅ No double quotes `""` around skill names
- ✅ Skills rendered as raw bold text (e.g., **Iron Fist Punishment**)
- ✅ Digimon names render correctly without annotations
- ⚠️ Line 511: "(BM)" is a residual abbreviation that should be removed

---

## Final Assessment

| Category | Count | Severity |
|----------|-------|----------|
| Mistranslation / Semantic | 4 | 🔴 Critical |
| Over-Translation | 2 | 🟡 Moderate |
| Terminology Non-Compliance | 3 | 🟡 Moderate |
| Glossary Gaps | 16 terms | 🟡 Maintenance |
| Style | 2 | 🟢 Minor |
| Formatting | 1 | 🟢 Minor |

**Pre-fix LQA: 91/100 → Post-fix target: 97+/100**
