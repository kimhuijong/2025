import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const mbtiFun = {
  "INTJ": { title: "마스터 전략가", emoji: "🧠" },
  "INFJ": { title: "꿈꾸는 철학자", emoji: "💭" },
  "ENTP": { title: "아이디어 폭발가", emoji: "💡" },
  "ISFJ": { title: "다정한 수호자", emoji: "🛡️" },
  "ESTP": { title: "모험가", emoji: "🌍" },
  "ENFP": { title: "에너지 뿜뿜", emoji: "⚡" },
  "ISTJ": { title: "완벽주의자", emoji: "📏" },
  "ESFP": { title: "파티의 주인공", emoji: "🎉" }
};

export default function App() {
  const [selectedMBTI, setSelectedMBTI] = useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-b from-yellow-200 to-pink-200 flex flex-col items-center p-6">
      <motion.h1
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-4xl font-bold mb-8 text-gray-800"
      >
        😎 나의 MBTI 캐릭터 찾기
      </motion.h1>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-3xl">
        {Object.keys(mbtiFun).map((mbti) => (
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
              <div className="text-6xl mb-4">{mbtiFun[selectedMBTI].emoji}</div>
              <h2 className="text-2xl font-bold text-gray-800">{mbtiFun[selectedMBTI].title}</h2>
              <p className="text-gray-600 mt-2">당신의 성격을 가장 잘 표현하는 캐릭터예요!</p>
            </CardContent>
          </Card>
        </motion.div>
      )}
    </div>
  );
}

