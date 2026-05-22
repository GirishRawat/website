# SOHMA Homepage Redesign — Implementation Complete

## Overview
The SOHMA homepage has been redesigned based on the "Homepage Narrative Direction May 2026" strategic brief. The new design introduces a **dual-mode visual system** (dark/light sections) that reflects SOHMA's two core realities: long-term infrastructure vision and current research validation.

## New Architecture

### 8-Section Structure (Dark/Light Alternation)

1. **HERO (DARK)** — Infrastructure Vision
   - Deep navy background with subtle blue/green gradient orbs
   - H1: "Behavioural Infrastructure for Emotionally Intelligent AI"
   - Subheadline emphasizes signal layer, not emotion detection
   - CTA: "Explore the Research" + "View the Technology"

2. **THE PROBLEM (LIGHT)** — Research Grounded
   - Panel format with two-column grid
   - Title: "AI responds to what you say. Not how you interact."
   - Explains the gap: AI lacks structured interpretation of behavioral signals
   - Tags: Hesitation, Pacing changes, Disengagement, Retry behaviour, etc.

3. **SIGNAL LAYER (DARK)** — Technical Infrastructure
   - 4-step flow with accent highlighting: Human Interaction → Signals → Layer → Adaptive AI
   - Emphasizes cross-environment consistency as core research challenge
   - Dark cards with glowing borders on navy background

4. **SOHMA LAB (LIGHT)** — Research Validation
   - 4 environment cards: Gaming, Learning, Conversational, Wellbeing
   - Title: "Where behavioural signals are studied and validated"
   - Framing: Environments for research, not separate products

5. **GOVERNANCE (DARK)** — Foundational Principles
   - 6 principles with checkmark indicators:
     - No diagnosis
     - No personality scoring
     - No hidden profiling
     - No automated intervention
     - Human oversight at every layer
     - Transparent, contextual outputs only
   - Emphasizes governance as design foundation, not compliance feature

6. **VISION (DARK)** — Long-Term Positioning
   - Infrastructure-oriented future applications list
   - Caveat: "Not a fully solved system. A research direction."
   - Side panel: Potential future environments

7. **COLLABORATE (LIGHT)** — Partnership
   - Two-column layout: copy + image
   - Targets: Research organisations, technical partners, governance bodies
   - CTA: "Start a conversation"

8. **FOOTER** — Updated Tagline
   - "Behavioural Signal Infrastructure for Adaptive AI Systems"

## Key Language Changes

### Removed (Per Document Direction)
- "Emotion detection"
- "Emotional regulation"
- "Understanding emotions"
- "Emotionally intelligent AI infrastructure" (in certain contexts)
- "CAPTCHA analogy"

### Updated To
- "Behavioural signals"
- "Interaction patterns"
- "Behavioural context"
- "Signal layer"
- "Emotional intelligence" (only in long-term vision context)
- Infrastructure-oriented framing

## Visual Design System

### Dark Mode Palette
- Background: `#06030F` (deep navy-black)
- Text: `rgba(255,255,255,.92)`
- Muted text: `rgba(255,255,255,.52)`
- Surface: `rgba(255,255,255,.05)`
- Border: `rgba(255,255,255,.09)`
- Eyebrow: `rgba(46,142,197,.85)` (bright blue)

### Light Mode (Preserved)
- Background: `#F5F7FB` (pale blue-grey)
- All existing brand colors maintained

### Wave Animations
- Hero section: Adapted for dark background
- Blue/green glowing orbs create cinematic feel
- Particle effects emphasize "signal" concept

## Responsive Design

### Breakpoints
- **1020px**: Two-column layouts become single column
- **980px**: Signal flow grid compresses, governance/lab grids adjust
- **780px**: Full mobile optimization, simplified spacing

### Mobile-First Approach
- All sections scale gracefully
- Typography uses clamp() for fluid sizing
- Touch-friendly button sizing (100% width on mobile)

## Navigation & Structure

### Navigation (Preserved)
- Sticky header with blur effect
- Links: Home, SOHMA Lab, Technology, Collaborate, Contact

### Internal Links Updated
- Hero CTAs link to sohma-lab.html and technology.html
- Lab section CTA to explore Lab
- Vision section CTA to collaborate.html
- All align with updated messaging

## Files Modified

- **index.html**: Complete redesign of code block content (lines 425-1478 in original)
  - Old: ~1000 lines
  - New: ~1500 lines
  - CSS: ~1200 lines (expanded for dark mode)
  - HTML: ~300 lines

## Strategic Alignment

### Document Requirements ✓
- [x] Two contrasting visual modes (dark/cinematic vs. light/research)
- [x] Language audit (removed "emotion detection", added "behavioral signals")
- [x] 8 narrative sections including governance and vision
- [x] Alternating dark/light structure for rhythm
- [x] Tone: Technically serious, research-led, ambitious but grounded
- [x] Visual hierarchy: Infrastructure-first, not product-first
- [x] Governance as foundational, not compliance layer

## Testing Checklist

Before launch, test:
- [ ] All 7 sections render correctly (desktop/tablet/mobile)
- [ ] Dark section backgrounds render correctly
- [ ] Wave animations perform smoothly
- [ ] All CTAs link to correct pages
- [ ] Responsive breakpoints function at 1020px, 980px, 780px
- [ ] Typography scales correctly (clamp() functions)
- [ ] Footer displays correctly
- [ ] Meta tags remain intact (Squarespace SEO)
- [ ] Navigation sticky header works
- [ ] Color contrast meets WCAG standards (especially dark text on dark bg)

## Next Steps

1. **Review in browser** - Test at www.sohma.xyz (or local dev)
2. **Check all links** - Verify CTAs navigate correctly
3. **Lighthouse audit** - Performance, accessibility, best practices
4. **Mobile testing** - iOS Safari, Android Chrome
5. **Stakeholder review** - Compare against original brief
6. **Push to production** - Deploy when approved

## Implementation Notes

- All Squarespace boilerplate preserved (meta tags, scripts, structure)
- CSS is minified where appropriate for performance
- JavaScript animations use CSS transforms (GPU-optimized)
- Accessibility maintained with semantic HTML and proper aria-labels
- No breaking changes to existing pages (sohma-lab.html, technology.html, etc.)

---

**Redesign Date**: May 2026  
**Based On**: Homepage Narrative Direction_May 2026.docx  
**Status**: Implementation Complete ✓
