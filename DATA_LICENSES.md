# 外部資料授權清單（Data Licenses）

本文件列出本專案使用之 **所有外部下載資料** 的來源、原始授權、可否商業化與 SHA-256 驗證值。  
執行 `python scripts/fetch_data.py` 後，檔案將被下載至 `data/` 目錄；請務必遵守各來源授權條款。

| 本地路徑 (download dir) | 來源網址 | 原始授權 | 商業用途 | SHA-256 (官方檔案雜湊) |
|------------------------|----------|----------|----------|------------------------|
| `data/DH_data/std_soln_He.p` | <https://github.com/hongwanliu/millicharged_DM_with_bath/> | 無授權（著作權所有） | **禁止** | `ed33184c1a……` |
| `data/rotmod_files/*` | <https://kapteyn.phys.rug.nl/gipsy/> | Kapteyn Institute Academic License | **禁止** | `8a812e9d48……` |
| `data/public_set/*` | <https://example.gov/open-data/> | CC0 1.0 Public Domain | 允許 | `——` |

## 條款摘要

* **無授權 / 著作權所有**  
  * 檔案僅能用於個人或學術研究；任何公開散布或商業使用須向原作者取得授權。
* **Kapteyn Institute Academic License**  
  * 允許學術研究與論文引用；禁止商業使用。完整條款請見 <https://kapteyn.phys.rug.nl/gipsy/license.html>。
* **CC0 1.0**  
  * 已放棄所有著作權，可自由使用、商業化、改作；但建議保留來源以利學術引用。

> **注意：**  
> 1. 若您對單一資料集的授權狀態有疑問，請先閱讀原始頁面條款或與權利人聯繫。  
> 2. 若需大規模商業使用本專案成果，請與我們商洽取得額外授權或替換資料來源。  
