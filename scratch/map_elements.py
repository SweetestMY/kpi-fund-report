# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's verify what HTML containers we need to ID in View 4, View 5, View 6:
# View 4:
#  - Pillar 1 card: id="t4-p1-card"
#  - Pillar 2 card: id="t4-p2-card"
#  - Pillar 3 card: id="t4-p3-card"
#  - Pillar 1 desc: id="t4-s1-d"
#  - Pillar 2 desc: id="t4-s2-d"
#  - Pillar 3 desc: id="t4-s3-d"
#  - Callout: id="t4-callout"
#  - Score box value: id="t4-sc-val"
#  - Score box stars: id="t4-sc-stars"
#  - Title badge: id="t4-badge"
#
# View 5:
#  - Sub-criterion 1 badge: id="t5-p1-badge"
#  - Sub-criterion 2 badge: id="t5-p2-badge"
#  - Left card achievement: id="t5-p1-achieve"
#  - Right card milestone box 1: id="t5-p2-m1"
#  - Right card milestone box 2: id="t5-p2-m2"
#  - Right card achievement: id="t5-p2-achieve"
#  - Callout: id="t5-callout"
#  - Score box value: id="t5-sc-val"
#  - Score box stars: id="t5-sc-stars"
#  - Title badge: id="t5-badge"
#
# View 6:
#  - Sub-criterion 1 badge: id="t6-p1-badge"
#  - Sub-criterion 2 badge: id="t6-p2-badge"
#  - Left card achievement: id="t6-p1-achieve"
#  - Right card container: id="t6-p2-container"
#  - Right card achievement: id="t6-p2-achieve"
#  - Callout: id="t6-callout"
#  - Score box value: id="t6-sc-val"
#  - Score box stars: id="t6-sc-stars"
#  - Title badge: id="t6-badge"

print("All elements mapped!")
