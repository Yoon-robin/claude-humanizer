---
type: llm
weight: 2
---

PASS if the reply is a rewritten Korean maintenance notice that stays formal (합니다체 / 하십시오체 throughout, the way a Korean company posts a notice), keeps every fact (the date and time exactly as "2026년 10월 14일(수) 02:00~06:00", that the website and the whole mobile app are affected, that no service can be used during maintenance, that the time may change and a separate notice will follow, and the apology), and reads more naturally than the original, for example by simplifying "향상을 위하여", "진행될 예정임을 알려드립니다", or "불가능하오니". Standard notice phrasing such as "안내드리겠습니다" or "양해 부탁드립니다" is fine.
FAIL if any sentence drops into 해요체 or 반말, if a fact is dropped, changed, or added, if the date or time is reformatted, or if it is no less stiff than the original.
