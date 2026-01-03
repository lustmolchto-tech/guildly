import fs from "fs";
import path from "path";

export default function handler(req, res) {
  const filePath = path.join(process.cwd(), "data", "maddeler.json");
  const file = fs.readFileSync(filePath, "utf8");
  const maddeler = JSON.parse(file);

  if (req.query.madde_no) {
    const madde = maddeler.find(m => m.madde_no == req.query.madde_no);
    if (madde) return res.status(200).json(madde);
    else return res.status(404).json({ detail: "Madde bulunamadı" });
  }

  res.status(200).json(maddeler);
}
