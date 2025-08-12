import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const mbtiJobs = {
  "INTJ": { job: "전략 기획자", emoji: "🧠" },
  "INFJ": { job: "심리 상담가", emoji: "💬" },
  "ENTP": { job: "창업가", emoji: "🚀" },
  "ISFJ": { job: "간호사", emoji: "🩺" },
  "ESTP": { job: "영업 전문가", emoji: "📈" },
  "ENFP": { job: "크리에이티브 디렉터", emoji: "🎨" },
  "ISTJ": { job: "회계사", emoji: "📊" },
  "ESFP": { job: "연예인", emoji: "🎤" }
};

export default function App() {
  const [selectedMBTI, setSelectedMBTI] = useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-b from-indigo-200 to-pink-200 flex flex-col items-center p-6">
      <motion.h1
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-4xl font-bold mb-8 text-gray-800"
      >
        💼 MBTI 기반 직업 추천
      </motion.h1>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-3xl">
        {Object.keys(mbtiJobs).map((mbti) => (
          <Button
            key={mbti}
            variant={selectedMBTI === mbti ? "default" : "outline"}
            className="p-4 text-lg font-semibold"
            onClick={() => setSelectedMBTI(mbti)}
          >
            {mbti}
          </Button>
        ))}
      </div>

      {selectedMBTI && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="mt-10"
        >
          <Card className="bg-white shadow-lg rounded-2xl p-6 text-center">
            <CardContent>
              <div className="text-6xl mb-4">{mbtiJobs[selectedMBTI].emoji}</div>
              <h2 className="text-2xl font-bold text-gray-800">{mbtiJobs[selectedMBTI].job}</h2>
              <p className="text-gray-600 mt-2">당신의 성향에 맞는 추천 직업입니다!</p>
            </CardContent>
          </Card>
        </motion.div>
      )}
    </div>
  );
}

