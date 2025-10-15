# Product Requirements Document (PRD) Extension (Set 2: Topic Discovery)

## 1. Document Overview

| Field | Value |
| :--- | :--- |
| **Product Name** | Topic-Based Summarizer (Set 2: Topic Discovery & Directory) |
| **Document Version** | 2.0 (Extension to v1.0) |
| **Date** | October 15, 2025 |
| **Focus** | Integrating Embedding, Clustering, and LLM Topic Labeling. |

---

## 2. Goals and Objectives

The primary objective of Set 2 is to move beyond raw text storage by implementing an **unsupervised topic discovery pipeline** to automatically categorize and structure the uploaded document content.

### A. Goals

* **Implement Embedding Pipeline:** Successfully transform text chunks into vector embeddings.
* **Establish Clustering Logic:** Use offline clustering techniques (k-means, HDBSCAN, or BERTopic) to group related chunks.
* **Create Topic Directory:** Automatically generate human-readable topic labels, keywords, and synonyms using a focused LLM call.
* **Enhance UI:** Present the discovered topics in a structured, browsable directory with detailed metadata.

### B. Dependencies (Set 1 Pre-requisites)

* **Stable Chunking:** The system must reliably chunk PDF/DOCX files as defined in FR 2.3 (Set 1).
* **Database Access:** The backend must have stable read/write access to the SQLite database.

---

## 3. Architectural and Technical Changes

### A. New Backend Components

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Embedding Model** | (e.g., Sentence-Transformers) | Converts text chunks into high-dimensional vectors. |
| **Clustering Library** | (e.g., `scikit-learn`, `hdbscan`, `bertopic`) | Executes the unsupervised learning logic to group embeddings. |
| **Topic Labelling Service** | LLM API Call | Generates topic names, keyphrases, and synonyms based on representative chunks. |

### B. Data Model Updates (SQLite Schema Extensions) 💾

The existing `FileChunks` table must be updated, and a new `Topics` table is required to store the clustered output.

| Table | Field | Data Type | Description | Change Type |
| :--- | :--- | :--- | :--- | :--- |
| **FileChunks** | `embedding` | BLOB (or JSON/TEXT) | The vector representation of the chunk. | **NEW** |
| | `cluster_id` | INTEGER | The ID assigned by the clustering algorithm. | **NEW** |
| **Topics** (NEW) | `id` | INTEGER | Primary key. | **NEW TABLE** |
| | `discussion_id` | INTEGER | Links to the parent discussion. | **NEW TABLE** |
| | `name` | TEXT | The LLM-generated name (e.g., "Pricing Strategy"). | **NEW TABLE** |
| | `keyphrases` | TEXT | JSON array of 5 keyphrases. | **NEW TABLE** |
| | `synonyms` | TEXT | JSON array of synonyms. | **NEW TABLE** |
| | `frequency` | INTEGER | Total count of chunks assigned to this topic. | **NEW TABLE** |

---

## 4. Functional Requirements (Set 2)

### FR 4. Embedding and Clustering Pipeline

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 4.1** | Chunk Embedding | Every time files are uploaded or processed, the raw text chunks must be converted into **vector embeddings**. The embeddings must be persisted in the `FileChunks` table. |
| **FR 4.2** | Offline Clustering | After embedding, a clustering algorithm (k-means, HDBSCAN, or BERTopic) must be applied to the embeddings for **all chunks** belonging to the discussion. |
| **FR 4.3** | Cluster ID Assignment | The resulting cluster ID must be stored in the `FileChunks` table for linkage. |

### FR 5. Topic Generation (LLM Labeling)

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 5.1** | Representative Retrieval | For each discovered cluster, the system must retrieve **20 to 50 chunks** closest to the cluster centroid (or most representative based on the clustering method). |
| **FR 5.2** | LLM Prompting | An LLM call must be executed using the representative chunks to generate a topic name ($\le 4$ words) and a list of keyphrases/synonyms. |
| **FR 5.3** | Topic Persistence | The generated topic name, keyphrases, synonyms, and the calculated frequency (chunk count) must be stored in the new **`Topics`** table. |

### FR 6. Topic Directory UI (React)

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **FR 6.1** | Dedicated View | The frontend must include a dedicated screen, tab, or panel named "**Topic Directory**" within the Discussion Interface View. |
| **FR 6.2** | Default Topic Display | The directory must display all discovered topics in **descending order of frequency**. |
| **FR 6.3** | Source & Frequency | Each displayed topic must clearly show its overall **Frequency** count and list all **Source Files** from which its chunks were derived. |
| **FR 6.4** | Grouping Toggle | A toggle/button must be provided to switch the display to the "**Group by File**" view. |
| **FR 6.5** | Grouped Topic Display | In the grouped view, topics must be displayed under collapsible file sections, sorted in **descending order of frequency** *within* that specific file's content. |

---

## 5. Testing Requirements (QA)

| Test Case | Description | Expected Outcome |
| :--- | :--- | :--- |
| **TC 4.1** | Full Pipeline Test | Upload **20 diverse files** (PDF/DOCX) to a new discussion. | The system must complete embedding, clustering, and topic labeling without crash. |
| **TC 4.2** | Topic Directory Population | Check the Topic Directory screen after processing. | The screen is populated with topics, frequency counts ($\ge 1$), and correct source file references. |
| **TC 4.3** | Frequency Sorting | Verify the default view's sorting. | Topics are correctly sorted in descending order based on overall frequency. |
| **TC 4.4** | Grouping and Sorting | Activate the "Group by File" view. | Topics are grouped under the correct source files, and topics within each file section are sorted by that file's specific frequency for the topic. |
| **TC 4.5** | Data Consistency | Check the SQLite database. | All chunks in `FileChunks` have a non-null `embedding` and `cluster_id`. The `Topics` table contains human-readable names, keyphrases, and synonyms. |