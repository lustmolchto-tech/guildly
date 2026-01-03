import fs from "fs";
import path from "path";

export default function handler(req, res) {
  try {
    const filePath = path.join(process.cwd(), "data", "tck.json");
    const file = fs.readFileSync(filePath, "utf8");
    const maddeler = JSON.parse(file);

    const madde_no = req.query.madde_no;
    if (!madde_no) return res.status(400).json({ detail: "madde_no parametresi gerekli" });

    const ceza = maddeler.find(m => m.madde_no == madde_no);
    if (!ceza) return res.status(404).json({ detail: "Ceza bilgisi yok" });

    res.status(200).json({ madde_no: ceza.madde_no, ceza: ceza.ceza });
  } catch (err) {
    res.status(500).json({ detail: "Sunucu hatası", error: err.message });
  }
}
