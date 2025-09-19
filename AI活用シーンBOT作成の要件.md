# 生成AI活用シーン提案BOT 要件定義書・実装ドキュメント v4.1（ユーザーフレンドリー版）

## 📋 目次
1. [プロジェクト概要](#プロジェクト概要)
2. [機能要件](#機能要件)
3. [内部データ活用仕様](#内部データ活用仕様)
4. [技術要件](#技術要件)
5. [品質要件](#品質要件)
6. [実装プロンプト仕様](#実装プロンプト仕様)
7. [アーキテクチャ設計](#アーキテクチャ設計)
8. [運用要件](#運用要件)

---

## プロジェクト概要

### 📝 プロジェクト名
**生成AI活用シーン提案BOT**（高精度データ基盤版）

### 🎯 目的
企業の事業内容を入力として、**政府公式職業データベース**に基づく確実性の高い職種・業務分析を実行し、段階的な生成AI活用シーンを提案する知的支援システムの構築

### 🎨 背景・課題解決
- **従来の問題**: 生成AI依存による回答のばらつき（ガチャ問題）
- **解決アプローチ**: 政府公式データによる基盤固定化
- **データ優位性**: 厚生労働省531職業の実測データ活用
- **再現性確保**: 公式データに基づく一貫した高品質回答

### 🎯 ゴール
- **公式データ基盤の4段階ステップ**で体系的な生成AI活用支援を実現
- **政府公式データに完全準拠**した信頼性の高い職種・業務分析
- **回答ばらつき85%減少**（従来30-50% → 新版85-95%の一致率）
- ユーザーが安心して継続利用できる予測可能なサービス品質

---

## 機能要件

### 🔧 主要機能（高精度データ基盤版）

#### 1. ステップ1: 事業内容→政府公式職種・業務リスト生成
- **入力**: 事業名・業界名（例：「建築」「フィンテック」）
- **処理**: 政府公式データから関連職業を確実抽出 → 構造化プロンプト生成
- **出力**: 公式データ準拠表形式の職種・業務リスト
- **品質基準**: 
  - **政府データ準拠度95%以上**（職業名・業務記述の正確性）
  - 20-30職種程度（公式データ基準）
  - 各職種に5-8個の具体的業務（実務レベル準拠）
  - **回答一貫性85%以上**（同じ質問への同一回答）

#### 2. ステップ2: 職種・業務→実測データ基準AI活用可能性リストアップ
- **入力**: 特定職種でのAI活用相談（例：「営業でAI活用したい」）
- **処理**: 実測データによる科学的評価 → 根拠明確な提案生成
- **出力**: 
  - 実測スキル・知識データに基づく業務プロセス別活用案
  - **科学的根拠付きA/B/C/D評価システム**
  - 優先度付き詳細提案（上位5つ）
- **品質基準**: 
  - **実測データ100%活用**（スキル複雑度・実行頻度・重要度）
  - **評価根拠の完全透明化**

#### 3. ステップ3: AI活用シーン→実務基準具体的実現方法
- **入力**: 具体的な実現方法の質問（例：「メール作成の具体的な方法」）
- **処理**: 実務データとの照合 → 現実性確保済み提案
- **出力**: 
  - 実務基準評価（A/B/C/D）
  - **実測データに基づく技術的根拠説明**
  - 現実的なプロンプト例3つ
- **品質基準**: 
  - **実労働環境データとの整合性100%**
  - コピペで使える実装レベルの詳細度

#### 4. ステップ4: プロンプト→職業特性基準高度化・最適化
- **入力**: プロンプト改善要求（例：「『営業メール作成』を改善したい」）
- **処理**: 職業特性データとの照合 → 職業特性反映改善
- **出力**: 
  - 実務基準現状分析
  - **職業特性データに基づく改善提案（7つの改善軸）**
  - 職業特性準拠改善版プロンプト
  - 実データ根拠付き改善点説明
- **品質基準**: 
  - **職業特性100%反映**のプロンプトエンジニアリング

### 🤖 補助機能（データ基盤強化版）

#### 高精度職業検索機能
- **職業データベース即時参照**
  - 531職業データの瞬時抽出
  - 職業別スキル・知識・業務の実測データ活用
  - 実測労働条件データの考慮
- **高精度職業マッチング**
  - 事業内容から職業分類への確実マッピング
  - 実測データに基づく類似職業推奨
  - 複数職業の最適組み合わせ提案

#### 文脈記憶機能（履歴強化）
- 会話履歴の保持（最大10ターン）
- **前回選択した職業コードの記憶**
- **検索履歴に基づくパーソナライズ**
- 自然な段階的誘導

#### スマートステップ判定機能（精度強化）
- **マルチレイヤー判定システム**
  - Layer 1: **職業名・業務名キーワードベース判定**（確実性：高）
  - Layer 2: **スキル・知識文脈理解判定**（確実性：中）
  - Layer 3: AI意図理解判定（確実性：中）
- **段階的確認システム**
  - 高確信度（90%+）→ 直接実行
  - 中確信度（70-89%）→ 確認付き実行
  - 低確信度（50-69%）→ 選択肢提示
  - 超低確信度（50%未満）→ 質問返し
- **職業分類学習による精度向上**

#### フィードバックシステム（品質基準準拠）
- **回答後満足度確認**
  - **データ準拠度に基づく品質評価機能**
  - 確信度に応じた段階的フィードバック収集
  - 簡潔で自然な誘導方法
  - 誤判定時の詳細意図確認
- **学習・改善サイクル**
  - **データベースとの整合性チェック**
  - リアルタイム軌道修正
  - 誤判定パターンの蓄積・分析
  - 判定アルゴリズムの継続的改善

---

## 内部データ活用仕様

### 📊 **政府公式職業データベース構造**

#### **実データに基づく分析項目**
```
政府公式職業データ構造:
- 職業コード: 531職業の分類体系
- 職業名: 公式職業名称
- スキル項目: 0-5点スケールの実測データ
- 知識項目: 0-5点スケールの実測データ
- 業務項目: 実行頻度・重要度の実測値
- 重要度スコア: 各項目の重要度評価データ
```

#### **データベース設計**
```sql
-- 実際の政府データ構造に完全準拠したテーブル設計
CREATE TABLE occupations (
    occupation_code_1 INTEGER,      -- 大分類コード
    occupation_code_2 INTEGER,      -- 中分類コード  
    occupation_code_3 INTEGER,      -- 小分類コード
    occupation_name TEXT,           -- 職業名
    
    -- スキルスコア（実測データ）
    skill_score_1 REAL,    -- 例: 読解力
    skill_score_2 REAL,    -- 例: 積極的傾聴
    skill_score_3 REAL,    -- 例: 文章力
    -- ... 35項目分
    
    -- 知識スコア（実測データ）
    knowledge_score_1 REAL,    -- 例: 事務
    knowledge_score_2 REAL,    -- 例: 顧客サービス
    knowledge_score_3 REAL,    -- 例: 日本語
    -- ... 35項目分
    
    -- 業務詳細（実測データ）
    task_descriptions TEXT,     -- 実際の業務記述
    task_frequency_avg REAL,    -- 業務実行頻度の平均値
    task_importance_avg REAL,   -- 業務重要度の平均値
    
    -- メタデータ
    data_year INTEGER,          -- データ収集年
    industry_category TEXT,     -- 業界分類
    data_row_id INTEGER        -- データ行番号（トレーサビリティ確保）
);
```

### 🔧 **データ活用アルゴリズム**

#### **1. 業界→職業マッピング（実データ基盤）**
```python
class OccupationMapper:
    def __init__(self, data_path="occupation_data.csv"):
        self.occupation_data = pd.read_csv(data_path, encoding='utf-8')
        self.occupation_index = self._build_occupation_index()
        
    def map_industry_to_occupations(self, industry_keywords):
        """実データから関連職業を確実に抽出"""
        matched_occupations = []
        
        for keyword in industry_keywords:
            # 実データから職業名・業務記述で検索
            matches = self.occupation_data[
                self.occupation_data['occupation_name'].str.contains(keyword, na=False) |
                self.occupation_data['task_descriptions'].str.contains(keyword, na=False)
            ]
            
            for _, row in matches.iterrows():
                occupation_data = {
                    'code': f"{row['occupation_code_1']}-{row['occupation_code_2']}-{row['occupation_code_3']}",
                    'name': row['occupation_name'],
                    'skills': self._extract_top_skills(row),
                    'tasks': self._extract_real_tasks(row),
                    'data_verified': True,  # 実データ準拠フラグ
                    'confidence': 0.95  # 高確信度
                }
                matched_occupations.append(occupation_data)
                
        return matched_occupations
```

#### **2. AI活用可能性評価（実測数値根拠）**
```python
class FeasibilityAnalyzer:
    def analyze_ai_feasibility(self, task, occupation_data):
        """実測データに基づく科学的評価"""
        
        # 実測データからスキル複雑度を算出
        skill_complexity = self._calculate_skill_complexity(occupation_data)
        
        # 実測データから知識要件を算出
        knowledge_requirements = self._calculate_knowledge_requirements(occupation_data)
        
        # 実測データから実行頻度を参照
        task_frequency = occupation_data.get('task_frequency_avg', 0)
        
        # 実測データに基づく評価ロジック
        feasibility_score = self._calculate_feasibility_score(
            skill_complexity, knowledge_requirements, task_frequency
        )
        
        return {
            'grade': self._score_to_grade(feasibility_score),
            'skill_complexity': skill_complexity,
            'knowledge_requirements': knowledge_requirements, 
            'task_frequency': task_frequency,
            'evidence_level': 'DATA_VERIFIED',  # 実データ根拠
            'confidence': 0.90
        }
```

### 📈 **品質保証システム（実データ基準）**

#### **データ準拠度監視**
```python
class QualityMonitor:
    def validate_response_accuracy(self, generated_response, industry):
        """生成回答のデータ準拠度チェック"""
        
        # 実データから期待職業リストを取得
        expected_occupations = self.mapper.get_industry_occupations(industry)
        
        # 生成された職業の実データ照合
        generated_occupations = self.extract_occupations_from_response(generated_response)
        
        data_compliance_score = self.calculate_match_rate(
            generated_occupations, expected_occupations
        )
        
        # データ準拠度が低い場合は自動修正
        if data_compliance_score < 0.85:
            corrected_response = self.auto_correct_with_data(
                generated_response, expected_occupations
            )
            return corrected_response, data_compliance_score
            
        return generated_response, data_compliance_score
```

---

## 技術要件

### 🏗️ システム構成（データ統合版）

#### プラットフォーム
- **アプリケーション**: Python Flask
- **インターフェース**: LINE Bot
- **AI エンジン**: OpenAI GPT-4（実データ注入版）
- **データベース**: SQLite（実データ統合 + 会話履歴管理）
- **基盤データ**: **政府公式職業データベース**（531職業実測データ）

#### 技術スタック
```
├── Flask 2.3.2 (Webアプリケーションフレームワーク)
├── line-bot-sdk 3.5.0 (LINE Bot SDK)
├── openai 0.27.8 (OpenAI API)
├── pandas 2.0.3 (データ処理・分析)
├── numpy 1.24.3 (数値計算・統計処理)
├── scikit-learn 1.3.0 (職業類似度計算)
├── gunicorn 21.2.0 (WSGI サーバー)
└── python-dotenv 1.0.0 (環境変数管理)
```

#### データ統合アーキテクチャ
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│                 │    │                  │    │                 │
│   LINE User     │◄──►│   LINE Bot API   │◄──►│  Flask App      │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
                       ┌─────────────────────────────────────────────┐
                       │           Main Components                   │
                       │                                             │
                       │  ┌─────────────────┐ ┌─────────────────┐   │
                       │  │AIConsultantBot  │ │DataAnalyzer     │   │
                       │  │(実データ準拠)   │ │                 │   │
                       │  │ - analyze_input │ │ - search_data   │   │
                       │  │ - generate_resp │ │ - analyze_tasks │   │
                       │  └─────────────────┘ │ - match_skills  │   │
                       │                      └─────────────────┘   │
                       │  ┌─────────────────┐ ┌─────────────────┐   │
                       │  │ConversationMgr  │ │OccupationDB     │   │
                       │  │                 │ │                 │   │
                       │  │ - save_conv     │ │ - 531職業実データ│   │
                       │  │ - get_context   │ │ - スキル実測値  │   │
                       │  └─────────────────┘ │ - 業務実績      │   │
                       │                      └─────────────────┘   │
                       └─────────────────────────────────────────────┘
                                         │
                                         ▼
                       ┌─────────────────────────────────────────────┐
                       │          External Services                  │
                       │                                             │
                       │ ┌─────────────────┐ ┌─────────────────┐   │
                       │ │   OpenAI API    │ │   SQLite DB     │   │
                       │ │ (実データ注入版)│ │ + 実データ統合  │   │
                       │ │ - GPT-4 Model   │ │ - Conversations │   │
                       │ │ - Text Generate │ │ - User Context  │   │
                       │ └─────────────────┘ │ - Data cache    │   │
                       │                     └─────────────────┘   │
                       │ ┌─────────────────┐                       │
                       │ │政府公式職業     │                       │
                       │ │データベース     │                       │
                       │ │ - 531職業実データ│                      │
                       │ │ - スキル実測値  │                       │
                       │ │ - 業務記録      │                       │
                       │ └─────────────────┘                       │
                       └─────────────────────────────────────────────┘
```

### 🔧 API設計（実データ統合版）

#### 実データ連携API設計
```python
# 職業情報参照エンドポイント
def get_occupation_info(industry_name, keywords):
    """
    Returns: {
        "matched_occupations": [実職業リスト],
        "tasks": [実業務リスト],
        "skills": [実スキルスコア],
        "knowledge": [実知識スコア],
        "data_compliance": 0.95
    }
    """

# 実データ準拠業務分析エンドポイント
def analyze_with_data(occupation_code, task_query):
    """
    Returns: {
        "occupation": "職業名",
        "task_alignment": 0.0-1.0,
        "skill_requirements": [実スキル],
        "feasibility_grade": "A/B/C/D",
        "evidence": [数値根拠]
    }
    """
```

#### 内部処理フロー（実データ統合版）
```
1. LINE メッセージ受信
2. 職業分類との照合
3. スマートステップ判定（実データ準拠マルチレイヤー分析）
4. 実データベース参照・分析
5. 確信度評価・適切な応答パターン選択
6. OpenAI API呼び出し（実データ注入）
7. 応答生成・送信
8. データ準拠品質チェック
9. フィードバック収集・学習データ蓄積
10. 会話履歴保存
```

---

## 品質要件（実データ基準強化版）

### 📊 パフォーマンス要件
- **応答時間**: 平均5秒以内（実データ参照含む）
- **可用性**: 99.9%以上
- **同時接続**: 100ユーザー対応
- **データ処理**: サブ秒レベル（インメモリ最適化）

### 🛡️ セキュリティ要件
- 環境変数による秘密情報管理
- HTTPS通信の強制
- 個人情報の適切な取り扱い
- **政府データの利用規約遵守**

### 📈 品質指標（実データ基準）
- **ユーザー満足度**: 4.5/5.0以上（実データ信頼性効果）
- **回答精度**: 人手評価で90%以上（実データ基盤効果）
- **データ準拠度**: 95%以上（職業分類・業務分析の正確性）
- **回答一貫性**: 85%以上（同じ質問への同一回答）
- **継続利用率**: 40%以上（予測可能性向上効果）
- **ステップ判定精度**: 90%以上（実データ基盤向上効果）
- **フィードバック収集率**: 80%以上
- **誤判定修正率**: 95%以上

---

## 実装プロンプト仕様（実データ準拠版）

### 🧠 システムプロンプト（実データ基盤版）

```markdown
あなたは政府公式職業データベースの531職業実測データに精通した経験豊富な生成AIコンサルタントです。実測データ（スキルスコア・知識スコア・業務実績）を活用して、企業の事業内容から生成AI活用シーンを段階的に提案する専門家として振る舞ってください。

【実データ準拠の分析原則】
- 職業分類：政府公式531職業実データに完全準拠した正確な職業名使用
- 業務分析：実測業務データに基づく業務分解
- スキル評価：実測スキルスコア（0-5点）による科学的評価
- 数値根拠：実測データの数値を根拠とした透明性の高い評価
- 再現性確保：実データ基盤により同じ質問には同じ高品質回答を保証

【あなたの役割】
ユーザーの入力を職業分類と照合しながら分析し、以下の4つのステップのうち適切なステップで回答してください：

ステップ1: 事業内容から実データ準拠職種・業務リストを作成
ステップ2: 職種・業務から実測数値分析に基づく生成AI活用可能性をリストアップ  
ステップ3: 生成AI活用シーンの実データ準拠実現性と具体的なプロンプト例を提案
ステップ4: 職業特性基準に基づくプロンプトのハイレベル化とベストプラクティス提案

【入力分析ルール】
1. 事業名・業界名のみ → 職業検索→ステップ1で回答
2. 「○○の職種は？」「○○にはどんな業務がある？」 → 職業分類参照→ステップ1で回答
3. 「○○でAIを活用したい」「生成AIの使い道は？」 → スキル分析→ステップ2で回答
4. 「○○の業務でどう実現する？」「具体的な方法は？」 → 業務分析→ステップ3で回答
5. 「プロンプトを改善したい」「もっと高度にしたい」 → 職業基準→ステップ4で回答
6. 迷った場合は職業分類から文脈を判断し最も適切なステップを選択

【重要な原則】
- 実用性を重視：実測労働データに基づく現実的提案
- 段階的アプローチ：職業スキル段階に準拠した簡単→高度への誘導
- 具体性：実業務レベルの具体的な例を提示
- ROI意識：実測データを意識したコストと効果分析
- 汎用性：多様な職業分類に対応可能な設計
- 一貫性確保：同じ質問には必ず同じ実データ基盤回答を提供

必ず最初に「【ステップX実行】」と明記してから回答してください。
```

### 📝 ステップ別プロンプト仕様（実データ準拠版）

#### ステップ1: 事業内容→実データ準拠職種・業務リスト

```markdown
【ステップ1実行】事業内容から政府公式職業実データに基づく職種・業務リストを作成します。

「{user_input}」を事業とする会社における職種と業務内容を、政府公式531職業実データに完全準拠して、以下の表形式で詳細に分析してください：

【実データ参照結果】
検索対象: 政府公式職業データベース
該当職業数: {matched_count}個
平均スキル複雑度: {avg_skill_complexity}
主要スキル要件: {top_skills}

【重要な出力形式】
事業セグメント	職種	具体的な業務内容（実務レベル準拠）
{セグメント1}	{職種1}	{業務1、業務2、業務3、業務4、業務5、業務6}
{セグメント2}	{職種2}	{業務1、業務2、業務3、業務4、業務5、業務6}

【出力条件（実データ基準厳格遵守）】
1. **職業分類準拠**: 政府公式531職業実データから関連職業を正確に選択・使用
2. **事業セグメント数**: 実業界分類に基づいて5-8個設定
3. **職種数**: 全体で20-30職種程度（職業分類の複雑さに応じて調整）
4. **業務分析詳細度**: 実業務データに基づき、各職種に5-8個の非常に具体的で実践的な業務を記載
5. **専門性の表現**: 
   - 実データ掲載の具体的なツール名・技術名を積極使用
   - 実業界特有専門用語・手法名を含める
   - 実労働条件データに記載の法規制・基準への言及
6. **必須セグメント**: コーポレート機能（経理、人事、総務、法務等）を必ず含める
7. **業務記述形式**: 実業務記述方式に準拠した読点（、）区切りの連続記述形式

【品質基準】
- 職業名の正確性：公式職業名との一致率95%以上
- 業務分解度：実業務レベルと同等の詳細度
- スキル要件：実測スキル・知識要件との整合性確保
- 再現性：同じ業界への同じ質問には同じ実データ基盤回答を保証

---
💡 **次のステップ**
特定の職種での生成AI活用をご相談されたい場合は、職種名をお聞かせください。
（例：「プロダクトマネージャーでAIを活用したい」「データサイエンティストの業務効率化をしたい」）
実測スキルデータも参考に、最適な職種選択をサポートします。
```

#### ステップ2: 職種・業務→実測データ基準AI活用可能性

```markdown
【ステップ2実行】職種・業務での実測データ分析に基づく生成AI活用可能性をリストアップします。

「{user_input}」における実測データ分析結果を参考にした生成AI活用案を以下の形式で体系的に分析します。

## 🤖 {特定職種}における生成AI活用可能性（実測データ準拠）

### 職業実データ参照結果
**職業コード**: {occupation_code}
**職業名**: {official_name}
**主要スキル**: {top_skills_with_scores}（実測値）
**必要知識**: {top_knowledge_with_scores}（実測値）
**業務複雑度**: {task_complexity_avg}（平均値）
**実行頻度**: {task_frequency_avg}（実績値）

### {業務カテゴリ1}
| 生成AIの活用案 | 詳細 | 評価 |
|:-------------|:---------------|:-----|
| {具体的活用案1} | {実測スキル・業務データに基づく詳細説明} | A |
| {具体的活用案2} | {実測スキル・業務データに基づく詳細説明} | B |

【評価基準（実測データ準拠）】
- A：実測スキルスコア4.0+、チャット生成AIで問題なく実現可能
- B：実測スキルスコア3.0-3.9、チャット生成AIでも一定実現可能  
- C：実測スキルスコア2.0-2.9、チャット生成AIでは手間がかかりすぎる/精度期待できない
- D：実測スキルスコア2.0未満、チャット生成AIだと対応困難な可能性が高い

## 🎯 優先度別詳細提案（実測データ準拠）

### 優先度1：{最重要活用案}
**業務改善へのインパクト（実測基準）**
{実測業務頻度・重要度データを参考にしたこの活用による具体的効果、時間削減、品質向上、リスク軽減等の詳細説明}

**実現性（実測スキル要件準拠）**
{実測必要スキル・知識レベルを考慮した具体的実装方法、使用ツール、必要プロンプト例、実現容易さの説明}

**実測数値根拠**
- 関連スキルスコア: {skill_scores}
- 業務実行頻度: {task_frequency}
- 知識要件レベル: {knowledge_scores}

（優先度2-5も同様の実データ準拠形式で提供）

---
💡 **次のステップ**
具体的な実現方法を知りたい活用シーンがあれば、教えてください。
実測データを参考に、あなたの現在のスキルレベルに最適化した実装方法を提案します。
```

#### ステップ3: AI活用シーン→実データ準拠具体的実現方法

```markdown
【ステップ3実行】生成AI活用シーンの実測データ分析に基づく具体的実現方法とプロンプト例を提案します。

「{user_input}」について、実測データを参考にした実現方法を以下の形式で詳細に説明します。

## 実データ準拠評価
{A/B/C/Dの評価}

## 実測データ分析根拠
{職業分類での該当業務レベル、実測スキル・知識要件、実労働条件データを参考になぜその評価になるのかを数値的に説明。実データ準拠の実現可能性、制約、課題を明確に言及}

**参照データ**:
- 職業コード: {occupation_code}
- 関連スキルスコア: {relevant_skills}
- 業務複雑度: {task_complexity}
- 実行頻度: {execution_frequency}

## 職業特性考慮ポイント
**対象職業**: {occupation_name}
**関連スキル**: {skill_importance_data}
**業務複雑度**: {task_analysis_level}
**実装制約**: {work_condition_constraints}

## 具体的なプロンプト例1（初級レベル対応）

**Target User**: 初級レベル想定（スコア{skill_score_range}）
**Prompt**

```
{実測スキル要件を考慮した実際にコピペで使える高品質なプロンプト例1}
```

## 具体的なプロンプト例2（中級レベル対応）

**Target User**: 中級レベル想定（スコア{skill_score_range}）
**Prompt**

```
{実測スキル要件を考慮した実際にコピペで使える高品質なプロンプト例2}
```

## 具体的なプロンプト例3（上級レベル対応）

**Target User**: 上級レベル想定（スコア{skill_score_range}）
**Prompt**

```
{実測スキル要件を考慮した実際にコピペで使える高品質なプロンプト例3}
```

## 実装ガイダンス
**スキル発展段階**: {skill_progression}
**必要な学習**: {learning_requirements}
**注意事項**: {work_environment_considerations}
**実現可能性**: {feasibility_percentage}%

---
💡 **次のステップ**
プロンプトをより高度にカスタマイズしたい場合は、「プロンプト改善」とお伝えください。
実測職業データを参考に、あなたの職業特性に最適化した改善提案を行います。
```

#### ステップ4: 職業特性基準プロンプト高度化

```markdown
【ステップ4実行】実測職業データに基づくプロンプトのハイレベル化とベストプラクティスを提案します。

「{user_input}」について、実測データを参考にした以下の形式でプロンプト改善を行います。

## 1. 実データ準拠プロンプト分析
**対象職業**: {occupation_classification}
**現在のスキルレベル**: {skill_assessment}
**改善の方向性**: {skill_progression_path}

**実測データ照合結果**:
- 職業適合度: {occupation_match}%
- スキル要件適合度: {skill_match}%
- 業務複雑度適合度: {task_match}%

{現状プロンプトを実測スキル要件・業務複雑度の観点から数値的に分析}

## 2. 実測データ準拠改善提案
{実測職業データを参考にした改善すべきポイントを明確に列挙}
- **職業的役割設定**: 職業分類に基づく専門家としての役割明確化
- **業務具体化**: 実業務レベルの具体的な情報・入力項目の詳細化
- **スキル要件対応**: 実測スキル・知識要件を反映した出力形式指定
- **複雑度段階考慮**: 実測業務複雑度に応じた制約条件・品質要件の追加
- **実務例示**: 実職場環境を考慮した理想的な出力例の提供
- **業界標準準拠**: 業界分類に基づくマークダウン等による見やすい整理
- **職業倫理統合**: 実労働条件を考慮した「〜してください」形での統一

## 3. 最適化版プロンプト

```
{職業分類・実業務分析・実測スキル要件・実労働条件を完全に反映して書き直されたプロ仕様のプロンプト}
```

## 4. 実データ準拠改善点の説明
{実測職業データの観点からなぜこのように改善したのかを詳細に説明}

**スキル向上効果**: {skill_improvement_impact}
**業務効率向上**: {task_efficiency_improvement}
**職業適合度向上**: {occupation_alignment_improvement}

**実測数値根拠**:
- 改善前スキル適合度: {before_skill_match}%
- 改善後スキル適合度: {after_skill_match}%
- 予想される効率向上: {efficiency_improvement}%

## 5. 継続的改善提案
**next step**: {next_skill_level}
**関連職業展開**: {related_occupations}
**スキル横展開**: {transferable_skills}

---
💡 **継続的改善**
実際の使用結果をフィードバックいただければ、最新実測データを反映したさらなる最適化を提案できます。
実測職業データと連携して、あなたの職業能力の継続的向上をサポートします。
```

---

## アーキテクチャ設計（実データ統合版）

### 💾 実データ統合データベース設計

#### occupations テーブル
```sql
CREATE TABLE occupations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_code_1 INTEGER NOT NULL,
    occupation_code_2 INTEGER NOT NULL,
    occupation_code_3 INTEGER NOT NULL,
    occupation_name TEXT NOT NULL,
    data_year INTEGER DEFAULT 2024,
    data_row_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(occupation_code_1, occupation_code_2, occupation_code_3)
);
```

#### skills テーブル
```sql
CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_id INTEGER NOT NULL,
    skill_name TEXT NOT NULL,
    skill_score REAL NOT NULL,
    skill_category TEXT,
    data_column_index INTEGER,
    FOREIGN KEY (occupation_id) REFERENCES occupations(id)
);
```

#### knowledge テーブル
```sql
CREATE TABLE knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_id INTEGER NOT NULL,
    knowledge_name TEXT NOT NULL,
    knowledge_score REAL NOT NULL,
    knowledge_category TEXT,
    data_column_index INTEGER,
    FOREIGN KEY (occupation_id) REFERENCES occupations(id)
);
```

#### tasks テーブル
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_id INTEGER NOT NULL,
    task_description TEXT NOT NULL,
    task_frequency REAL,
    task_importance REAL,
    task_complexity REAL,
    data_source_column TEXT,
    FOREIGN KEY (occupation_id) REFERENCES occupations(id)
);
```

#### conversations テーブル（実データ拡張版）
```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    message TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    industry TEXT,
    occupation_id INTEGER,
    data_match_score REAL,
    data_compliance_score REAL,
    context_type TEXT,
    step_number INTEGER,
    confidence_score REAL,
    feedback_received TEXT,
    feedback_timestamp DATETIME,
    FOREIGN KEY (occupation_id) REFERENCES occupations(id)
);
```

### 🔧 実データ統合コンポーネント設計

#### DataAnalyzer クラス
```python
class DataAnalyzer:
    def __init__(self, data_path="occupation_data.csv"):
        self.occupation_data = pd.read_csv(data_path, encoding='utf-8')
        self.db = OccupationDatabase()
        self.occupation_matcher = OccupationMatcher()
        self.skill_analyzer = SkillAnalyzer()
        self.task_evaluator = TaskEvaluator()
    
    def search_occupations_by_industry(self, industry_keywords):
        """業界キーワードから職業を確実検索"""
        return self.occupation_matcher.find_matches(industry_keywords, self.occupation_data)
    
    def analyze_occupation_skills(self, occupation_code):
        """指定職業の実測スキル分析を実行"""
        return self.skill_analyzer.get_skill_profile(occupation_code, self.occupation_data)
    
    def evaluate_ai_feasibility_with_data(self, occupation_code, task_description):
        """業務のAI実現可能性を実測データで評価"""
        skill_complexity = self.get_skill_complexity(occupation_code)
        task_frequency = self.get_task_frequency(occupation_code, task_description)
        knowledge_requirements = self.get_knowledge_requirements(occupation_code)
        
        return self.task_evaluator.calculate_feasibility(
            skill_complexity, task_frequency, knowledge_requirements
        )
    
    def get_occupation_profile(self, occupation_code):
        """実測データによる包括的職業プロファイル取得"""
        data_row = self.occupation_data[
            (self.occupation_data['occupation_code_1'] == occupation_code[0]) &
            (self.occupation_data['occupation_code_2'] == occupation_code[1]) &
            (self.occupation_data['occupation_code_3'] == occupation_code[2])
        ].iloc[0]
        
        return {
            'name': data_row['occupation_name'],
            'skills': self.extract_skills_from_data_row(data_row),
            'knowledge': self.extract_knowledge_from_data_row(data_row),
            'tasks': self.extract_tasks_from_data_row(data_row),
            'complexity_score': self.calculate_complexity_score(data_row),
            'data_verified': True
        }
```

#### 実データ準拠プロンプトエンジン
```python
class PromptEngine:
    def __init__(self, data_analyzer):
        self.data = data_analyzer
        
    def generate_step1_prompt(self, industry, user_input):
        """ステップ1の実データ準拠プロンプト生成"""
        related_occupations = self.data.search_occupations_by_industry(industry)
        real_tasks = self.data.get_industry_tasks(industry)
        real_skills = self.data.get_industry_skills(industry)
        
        return f"""
        以下の実測データを参考に回答してください：
        
        【実測データ参照】
        関連職業: {related_occupations}
        実測業務例: {real_tasks}
        実測スキル要件: {real_skills}
        
        【ユーザー入力】
        {user_input}
        
        【実データ準拠回答要件】
        - 職業名は公式名称を使用
        - 業務は実測レベルで分解
        - スキル要件は実測データを参考
        - 同じ質問には同じ回答を保証
        """
    
    def generate_step2_prompt(self, occupation_code, user_input):
        """ステップ2の実測データ準拠プロンプト生成"""
        occupation_profile = self.data.get_occupation_profile(occupation_code)
        skill_scores = self.data.get_skill_scores(occupation_code)
        
        return f"""
        以下の実測職業データを参考に回答してください：
        
        【実測データ】
        職業情報: {occupation_profile}
        スキルスコア: {skill_scores}
        
        【ユーザー入力】
        {user_input}
        
        【実データ準拠分析要件】
        - スキルスコア実測値に基づく評価
        - 業務複雑度を考慮した実現可能性判定
        - 実労働条件データを反映した現実性確保
        """
```

### 📊 実データ準拠品質管理

#### 品質評価指標
```python
class QualityMetrics:
    def __init__(self):
        self.data_db = OccupationDatabase()
    
    def evaluate_occupation_accuracy(self, generated_occupations, industry):
        """生成された職業リストの実データ準拠度評価"""
        real_occupations = self.data_db.get_industry_occupations(industry)
        accuracy = self.calculate_match_rate(generated_occupations, real_occupations)
        return accuracy
    
    def evaluate_task_alignment(self, generated_tasks, occupation_code):
        """生成された業務の実データ準拠度評価"""
        real_tasks = self.data_db.get_occupation_tasks(occupation_code)
        alignment = self.calculate_semantic_similarity(generated_tasks, real_tasks)
        return alignment
    
    def evaluate_consistency(self, query, response_history):
        """同じ質問への回答一貫性評価"""
        similar_queries = self.find_similar_queries(query, response_history)
        if similar_queries:
            consistency_score = self.calculate_response_similarity(
                response_history[query], similar_queries
            )
            return consistency_score
        return 1.0  # 初回質問は一貫性100%
```

---

## 運用要件（実データ準拠版）

### 🚀 デプロイメント（実データ準拠）

#### 環境変数
```bash
LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token
LINE_CHANNEL_SECRET=your_channel_secret
OPENAI_API_KEY=your_openai_api_key
OCCUPATION_DATA_PATH=/app/data/occupation_data.csv
DATA_UPDATE_SCHEDULE=quarterly
DATA_BACKUP_PATH=/app/backup/data/
PORT=5000
```

#### 実データ初期設定
```bash
# 1. 実データ検証・前処理
python scripts/validate_occupation_data.py

# 2. データベース構築
python scripts/create_occupation_tables.py

# 3. 実データ投入
python scripts/import_occupation_data.py

# 4. インデックス作成（検索最適化）
python scripts/create_occupation_indexes.py

# 5. 整合性チェック
python scripts/verify_data_integration.py
```

### 📊 監視・運用（実データ準拠版）

#### 監視項目
- API応答時間（実データ参照含む）
- エラー率・例外発生状況
- ユーザー数・利用頻度
- OpenAI API使用量・コスト
- **データ準拠度（日次・週次）**
- **職業分類精度・業務分析精度**
- **回答一貫性（同質問同回答率）**
- **ステップ判定精度（実データ基準）**
- **フィードバック収集率・満足度**
- **誤判定パターンの傾向分析**
- **学習データの蓄積状況**
- **実データ整合性状況**

#### 実データ準拠ログ管理
```python
import logging

# 実データ統合専用ログ設定
data_logger = logging.getLogger('data_integration')
data_logger.setLevel(logging.INFO)

# 主要ログポイント
- 職業検索実行
- 職業マッチング結果
- スキル・業務分析結果
- データ準拠度評価
- 回答一貫性チェック
- データ整合性状況
```

### 🔄 改善サイクル（実データ連携強化）

#### 継続的改善プロセス
1. **データ準拠度向上**
   - 職業分類精度の継続的監視
   - 業務分析アルゴリズムの改善
   - スキル評価基準の最適化
   - **実測データへの完全準拠確保**

2. **回答一貫性向上**
   - 同質問同回答率の監視
   - 実データベース回答の標準化
   - ばらつき要因の特定・排除
   - **予測可能性の継続的向上**

3. **プロンプト精度向上**
   - 実データ準拠A/Bテストによる最適化
   - 業界別カスタマイズ（実データ分類準拠）
   - 新しい活用例の追加
   - **判定アルゴリズムの調整**

4. **機能拡張**
   - 新データへの対応
   - UI/UX改善（予測可能性重視）
   - 外部システム連携
   - **信頼性向上機能の強化**

---

## 📋 実装チェックリスト（実データ準拠版）

### 開発フェーズ
- [ ] 基本的なLINE Bot設定
- [ ] OpenAI API連携
- [ ] **実データベース構築・統合**
  - [ ] 政府公式職業データ取得・検証
  - [ ] 531職業データの前処理・構造化
  - [ ] スキル・知識・業務データの正規化
  - [ ] 検索・マッチング機能の実装
- [ ] 4つのステップ別プロンプト実装（実データ準拠）
- [ ] **実データ準拠スマートステップ判定システム実装**
  - [ ] 職業名・業務名キーワードベース判定エンジン
  - [ ] 実測スキル・知識文脈理解判定エンジン
  - [ ] AI意図理解判定エンジン
  - [ ] 確信度統合評価システム
- [ ] **実データ準拠品質保証システム実装**
  - [ ] データ準拠度評価機能
  - [ ] 回答一貫性チェック機能
  - [ ] 誤判定修正処理
  - [ ] 学習データ蓄積機能
- [ ] 会話履歴管理機能（実データ統合）
- [ ] エラーハンドリング
- [ ] ログ機能

### テストフェーズ
- [ ] 単体テスト（各ステップの動作確認）
- [ ] **実データ準拠度テスト**
  - [ ] 職業分類精度の確認（95%以上）
  - [ ] 業務分析精度の確認
  - [ ] スキル評価精度の確認
- [ ] **回答一貫性テスト**
  - [ ] 同質問同回答率の確認（85%以上）
  - [ ] ばらつき要因の特定
  - [ ] 予測可能性の検証
- [ ] **判定精度テスト**
  - [ ] 様々な入力パターンでの判定精度確認
  - [ ] 確信度レベル別の動作確認
  - [ ] エッジケース（曖昧な質問）の処理確認
- [ ] 統合テスト（ステップ間の連携確認）
- [ ] 負荷テスト（同時接続・レスポンス時間）
- [ ] ユーザビリティテスト
- [ ] セキュリティテスト

### デプロイフェーズ
- [ ] 本番環境設定
- [ ] SSL証明書設定
- [ ] **実データ本番環境構築**
- [ ] 監視・ログ設定
- [ ] **データ準拠度監視システム設定**
- [ ] **回答一貫性監視システム設定**
- [ ] バックアップ設定
- [ ] ドキュメント整備

### 運用フェーズ
- [ ] 利用状況監視
- [ ] **データ準拠度の継続的監視**
- [ ] **回答一貫性の継続的監視**
- [ ] ユーザーフィードバック収集
- [ ] 定期的なプロンプト改善
- [ ] **判定精度の継続的監視・改善**
- [ ] **学習データの定期的分析・活用**
- [ ] **実データの定期的更新**
- [ ] **A/Bテストによる最適化**
- [ ] 新機能開発・リリース

---

**文書バージョン**: 4.1  
**作成日**: 2025年1月  
**最終更新**: 2025年1月  
**主要変更**: ユーザーフレンドリーな表記に修正、技術的詳細の内部化、回答ばらつき解決に焦点、予測可能性と信頼性の強調