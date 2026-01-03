import fs from "fs";
import path from "path";

export default function handler(req, res) {
  const filePath = path.join(process.cwd(), "data", "cezalar.json");
  const file = fs.readFileSync(filePath, "utf8");
  const cezalar = JSON.parse(file);

  const madde_no = req.query.madde_no;
  const ceza = cezalar.find(c => c.madde_no == madde_no);

  if (ceza) return res.status(200).json(ceza);
  else return res.status(404).json({ detail: "Ceza bilgisi yok" });
}
