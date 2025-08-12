import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const MBTI_DATA = {
  INTJ: { emoji: "🧠", title: "마스터 전략가", desc: "냉철한 계획가 — 큰 그림과 시스템 설계에 능해요." },
  INTP: { emoji: "🔬", title: "논리 탐구자", desc: "아이디어 실험실 — 이론과 개념을 파헤치길 좋아해요." },
  ENTJ: { emoji: "🏳️‍🌈", title: "카리스마 리더", desc: "목표 지향적 리더 — 팀을 끌고 결과를 만들어내요." },
  ENTP: { emoji: "💡", title: "아이디어 폭발가", desc: "토론과 창의적 발상으로 분위기를 띄워요." },
  INFJ: { emoji: "💭", title: "꿈꾸는 철학자", desc: "깊은 통찰과 공감으로 의미를 찾는 타입이에요." },
  INFP: { emoji: "🌱", title: "이상주의자", desc: "가치 중심의 감성가 — 자신만의 세계관을 소중히 해요." },
  ENFJ: { emoji: "🌟", title: "매력적인 촉진자", desc: "사람을 돕고 동기를 부여하는 데 능해요." },
  ENFP: { emoji: "⚡", title: "에너지 뿜뿜", desc: "호기심 많고 열정적인 사람 — 가능성을 즐겨 찾아요." },
  ISTJ: { emoji: "📏", title: "완벽주의자", desc: "신중하고 책임감이 강한, 규칙을 잘 지키는 타입이에요." },
  ISFJ: { emoji: "🛡️", title: "다정한 수호자", desc: "섬세하고 헌신적 — 주변을 돌보는 일을 잘해요." },
  ESTJ: { emoji: "⚖️", title: "실무 관리자", desc: "조직을 운영하고 효율을 만드는 데 능숙해요." },
  ESFJ: { emoji: "🤝", title: "따뜻한 조력자", desc: "사교적이고 배려심 많아 사람들과의 연결을 중요시해요." },
  ISTP: { emoji: "🔧", title: "현장 해결사", desc: "실용적이고 즉흥적 — 문제를 손으로 해결하는 걸 좋아해요." },
  ISFP: { emoji: "🎨", title: "감성의 예술가", desc: "예술적이고 현재를 즐기는 감각적인 사람입니다." },
  ESTP: { emoji: "🌍", title: "모험가", desc: "행동파 현실주의자 — 도전과 속도감을 즐깁니다." },
  ESFP: { emoji: "🎉", title: "파티의 주인공", desc: "밝고 사교적 — 분위기를 살리는 재주가 있어요." }
};

export default function MBTIFunApp() {
  const [selected, setSelected] = useState(null);
  const [copied, setCopied] = useState(false);

  const mbtiKeys = Object.keys(MBTI_DATA);

  function pickRandom() {
    const r = mbtiKeys[Math.floor(Math.random() * mbtiKeys.length)];
    setSelected(r);
    setCopied(false);
  }

  async function copyResult() {
    if (!selected) return;
    const text = `${selected} ${MBTI_DATA[selected].emoji} — ${MBTI_DATA[selected].title}: ${MBTI_DATA[selected].desc}`;
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (e) {
      alert("복사에 실패했습니다. 수동으로 드래그해서 복사해 주세요.");
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-yellow-200 to-pink-200 flex flex-col items-center p-6">
      <motion.header
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="w-full max-w-4xl"
      >
        <h1 className="text-4xl font-extrabold text-gray-900 mb-2 text-center">😎 나의 MBTI 캐릭터 찾기</h1>
        <p className="text-center text-gray-700 mb-6">MBTI를 눌러서 당신의 캐릭터를 확인해보세요 — 그냥 놀기 좋게 만든 재미용 앱이에요.</p>
      </motion.header>

      <main className="w-full max-w-4xl">
        <div className="grid grid-cols-4 sm:grid-cols-8 gap-3 mb-6">
          {mbtiKeys.map((m) => (
            <Button
              key={m}
              variant={selected === m ? "default" : "outline"}
              className={`p-3 text-sm font-semibold ${selected === m ? "ring-2 ring-offset-2" : ""}`}
              onClick={() => { setSelected(m); setCopied(false); }}
            >
              {m}
            </Button>
          ))}
        </div>

        <div className="flex justify-center gap-3 mb-6">
          <Button onClick={pickRandom} className="px-4">🎲 랜덤</Button>
          <Button onClick={() => { setSelected(null); setCopied(false); }} className="px-4">✖️ 초기화</Button>
          <Button onClick={copyResult} className="px-4">📋 결과 복사</Button>
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.4 }}
          className="flex justify-center"
        >
          {selected ? (
            <Card className="bg-white shadow-xl rounded-2xl p-6 w-full max-w-xl">
              <CardContent>
                <div className="flex items-center gap-6">
                  <div className="text-7xl">{MBTI_DATA[selected].emoji}</div>
                  <div>
                    <h2 className="text-2xl font-bold text-gray-900">{selected} — {MBTI_DATA[selected].title}</h2>
                    <p className="text-gray-700 mt-2">{MBTI_DATA[selected].desc}</p>
                    <p className="text-sm text-gray-500 mt-3">Tip: 친구와 비교해보면 더 재밌어요 :)</p>
                  </div>
                </div>
                <div className="mt-4 flex gap-3 justify-end">
                  <Button onClick={() => { navigator.share ? navigator.share({ title: "나의 MBTI 캐릭터", text: `${selected} — ${MBTI_DATA[selected].title}`, url: window.location.href }) : alert('공유를 지원하지 않는 환경이에요.'); }}>🔗 공유</Button>
                  <Button onClick={copyResult}>{copied ? "✅ 복사됨" : "📋 복사"}</Button>
                </div>
              </CardContent>
            </Card>
          ) : (
            <Card className="bg-white/80 shadow-md rounded-2xl p-6 w-full max-w-xl">
              <CardContent>
                <div className="text-center text-gray-700">MBTI를 선택하거나 <strong>랜덤</strong> 버튼을 눌러 결과를 확인해보세요!</div>
              </CardContent>
            </Card>
          )}
        </motion.div>

        <footer className="mt-8 text-center text-gray-600 text-sm">
          만든이: 당신의 멋진 앱 • 그냥 재미로 쓰세요 ✨
        </footer>
      </main>
    </div>
  );
}
