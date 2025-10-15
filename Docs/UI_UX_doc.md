# UI/UX Design System Documentation

## Design System Overview

This design system is based on **Google Material Design 3** with a **dark mode** theme, specifically tailored for the Topic-Based Summarizer MVP. The design emphasizes clarity, accessibility, and a modern user experience while maintaining consistency across all components.

## Color Palette

### Primary Colors

| Color Name | Hex Code | Usage | Material Design Level |
|------------|----------|-------|----------------------|
| **Color 1** | `#0D0D0D` | Background for panels and base layer | Surface 0 |
| **Color 2** | `#1A1A1A` | Background for overlapping panels | Surface 1 |
| **Color 3** | `#262626` | Default button background | Surface 2 |
| **Color 4** | `#333333` | Button hover state | Surface 3 |
| **Color 5** | `#404040` | Button active/pressed state | Surface 4 |
| **Color 6** | `#4D4D4D` | Highest surface elevation (rare use) | Surface 5 |
| **Color 7** | `#FFFFFF` | Primary text and highlight elements | On Surface |

### Accent Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Accent Magenta** | `#C82FFF` | Checkboxes, toggles, and accent elements |
| **X Gradient Start** | `#C82FFF` | Primary CTA buttons |
| **X Gradient End** | `#00AAFF` | Primary CTA buttons |
| **Placeholder** | `#A8A8A8` | Borders, hint text, and secondary elements |

### Color Usage Guidelines

#### Background Hierarchy
- **Layer 0**: Use Color 1 (`#0D0D0D`) as the base background
- **Layer 1**: Use Color 2 (`#1A1A1A`) for panels that overlap the base
- **Layer 2**: Use Color 3 (`#262626`) for clickable elements in default state
- **Layer 3**: Use Color 4 (`#333333`) for hover states
- **Layer 4**: Use Color 5 (`#404040`) for active/pressed states

#### Text Hierarchy
- **Primary Text**: Color 7 (`#FFFFFF`) for main content
- **Secondary Text**: Color 7 with 70% opacity for supporting text
- **Hint Text**: Placeholder color (`#A8A8A8`) for input hints
- **Error Text**: Accent Magenta (`#C82FFF`) for error states

## Typography

### Font Family
- **Primary Font**: Montserrat (Google Fonts)
- **Weights**: Regular (400), Medium (500), Semi-Bold (600)
- **Fallback**: system-ui, -apple-system, sans-serif

### Typography Scale

| Element | Font Weight | Size | Line Height | Usage |
|---------|-------------|------|-------------|-------|
| **H1** | Semi-Bold (600) | 32px | 1.2 | Main page titles |
| **H2** | Medium (500) | 24px | 1.3 | Section headers |
| **H3** | Medium (500) | 20px | 1.4 | Subsection headers |
| **H4** | Medium (500) | 18px | 1.4 | Component titles |
| **Body Large** | Regular (400) | 16px | 1.5 | Primary content |
| **Body** | Regular (400) | 14px | 1.5 | Secondary content |
| **Body Small** | Regular (400) | 12px | 1.4 | Supporting text |
| **Caption** | Regular (400) | 10px | 1.3 | Labels and captions |

### Typography Guidelines
- Use Semi-Bold only for very large headings (H1)
- Use Medium for most headlines and important text
- Maintain consistent line heights for readability
- Ensure sufficient contrast ratios (WCAG AA compliance)

## Component Design System

### Buttons

#### Primary Buttons
- **Background**: X Gradient (`#C82FFF` to `#00AAFF`)
- **Text Color**: Color 7 (`#FFFFFF`)
- **Shape**: Capsule buttons with maximum corner radius
- **Padding**: 12px horizontal, 8px vertical
- **States**:
  - Default: Full gradient
  - Hover: Slightly lighter gradient
  - Active: Slightly darker gradient
  - Disabled: 50% opacity

#### Secondary Buttons
- **Default State**: Color 3 (`#262626`)
- **Hover State**: Color 4 (`#333333`)
- **Active State**: Color 5 (`#404040`)
- **Text Color**: Color 7 (`#FFFFFF`)
- **Shape**: Capsule buttons with maximum corner radius

#### Button Sizes
- **Large**: 48px height, 16px horizontal padding
- **Medium**: 40px height, 12px horizontal padding
- **Small**: 32px height, 8px horizontal padding

### Input Fields

#### Text Inputs
- **Background**: Color 2 (`#1A1A1A`)
- **Border**: 0.5px solid Placeholder (`#A8A8A8`)
- **Border Radius**: 2-4px (rectangular with comfortable rounding)
- **Padding**: 12px horizontal, 8px vertical
- **Text Color**: Color 7 (`#FFFFFF`)
- **Placeholder**: Placeholder color (`#A8A8A8`)

#### Input States
- **Default**: Placeholder border
- **Focus**: Accent Magenta border (`#C82FFF`)
- **Error**: Accent Magenta border with error message
- **Disabled**: 50% opacity

### Cards and Panels

#### Discussion Cards
- **Background**: Color 2 (`#1A1A1A`)
- **Border**: 0.5px solid Placeholder (`#A8A8A8`)
- **Border Radius**: 8px
- **Padding**: 16px
- **Shadow**: Subtle elevation shadow
- **Hover**: Slight background color change to Color 3

#### File Upload Area
- **Background**: Color 2 (`#1A1A1A`)
- **Border**: 2px dashed Placeholder (`#A8A8A8`)
- **Border Radius**: 8px
- **Padding**: 24px
- **Hover**: Border color changes to Accent Magenta

### Chat Interface

#### Message Bubbles
- **User Messages**:
  - Background: X Gradient (`#C82FFF` to `#00AAFF`)
  - Text: Color 7 (`#FFFFFF`)
  - Alignment: Right
  - Border Radius: 16px (capsule shape)

- **AI Messages**:
  - Background: Color 3 (`#262626`)
  - Text: Color 7 (`#FFFFFF`)
  - Alignment: Left
  - Border Radius: 16px (capsule shape)

#### Chat Input
- **Background**: Color 2 (`#1A1A1A`)
- **Border**: 1px solid Placeholder (`#A8A8A8`)
- **Border Radius**: 20px (capsule shape)
- **Padding**: 12px horizontal, 8px vertical

### NEW: Topic Directory Interface

#### Topic Directory Container
- **Background**: Color 1 (`#0D0D0D`) - Base layer
- **Border**: 0.5px solid Placeholder (`#A8A8A8`)
- **Border Radius**: 8px
- **Padding**: 16px
- **Max Height**: 70vh with scrollable content

#### Topic Cards
- **Background**: Color 2 (`#1A1A1A`)
- **Border**: 0.5px solid Placeholder (`#A8A8A8`)
- **Border Radius**: 8px
- **Padding**: 16px
- **Margin**: 8px between cards
- **Hover**: Background changes to Color 3 (`#262626`)

#### Topic Header
- **Topic Name**: 
  - Font: Medium (500), 18px
  - Color: Color 7 (`#FFFFFF`)
  - Text: Semi-bold for topic titles

- **Frequency Badge**:
  - Background: Accent Magenta (`#C82FFF`)
  - Text: Color 7 (`#FFFFFF`)
  - Border Radius: 12px (capsule)
  - Padding: 4px 8px
  - Font: Regular (400), 12px

#### Topic Metadata
- **Keyphrases**:
  - Background: Color 3 (`#262626`)
  - Text: Color 7 (`#FFFFFF`) with 80% opacity
  - Border Radius: 4px
  - Padding: 4px 8px
  - Font: Regular (400), 12px
  - Display: Inline tags with 4px spacing

- **Source Files**:
  - Text: Placeholder color (`#A8A8A8`)
  - Font: Regular (400), 12px
  - Icon: `description` (16px)
  - Display: List with bullet points

#### Group by File Toggle
- **Toggle Container**:
  - Background: Color 2 (`#1A1A1A`)
  - Border: 0.5px solid Placeholder (`#A8A8A8`)
  - Border Radius: 20px (capsule)
  - Padding: 8px 16px

- **Toggle Button**:
  - Active: Accent Magenta (`#C82FFF`)
  - Inactive: Color 4 (`#333333`)
  - Text: Color 7 (`#FFFFFF`)
  - Border Radius: 16px (capsule)
  - Padding: 6px 12px
  - Font: Medium (500), 14px

#### File Group Sections
- **Collapsible Headers**:
  - Background: Color 3 (`#262626`)
  - Text: Color 7 (`#FFFFFF`)
  - Font: Medium (500), 16px
  - Padding: 12px 16px
  - Border Radius: 8px
  - Icon: `expand_more` / `expand_less` (20px)

- **File Topic Lists**:
  - Background: Color 2 (`#1A1A1A`)
  - Padding: 12px
  - Border Radius: 8px
  - Margin: 8px 0

## Icons and Visual Elements

### Icon Guidelines
- **Library**: Google Material Design Icons
- **Weight**: 200 (light)
- **Fill**: Off (outline style)
- **Size**: 24px for standard icons, 16px for small icons
- **Color**: Color 7 (`#FFFFFF`) for primary, Placeholder (`#A8A8A8`) for secondary

### Common Icons
- **Add**: `add` (create new discussion)
- **Upload**: `cloud_upload` (file upload)
- **Chat**: `chat_bubble` (AI chat)
- **Delete**: `delete` (remove items)
- **Edit**: `edit` (modify content)
- **Send**: `send` (chat messages)
- **File**: `description` (document files)
- **NEW: Topic Discovery Icons**:
  - **Topics**: `topic` (topic directory)
  - **Frequency**: `analytics` (frequency display)
  - **Group**: `group_work` (group by file)
  - **Expand**: `expand_more` / `expand_less` (collapsible sections)
  - **Keyphrases**: `label` (topic metadata)
  - **Process**: `auto_awesome` (topic discovery pipeline)

## Layout and Spacing

### Grid System
- **Container Max Width**: 1200px
- **Gutter**: 16px
- **Breakpoints**:
  - Mobile: 320px - 768px
  - Tablet: 768px - 1024px
  - Desktop: 1024px+

### Spacing Scale
- **XS**: 4px
- **S**: 8px
- **M**: 16px
- **L**: 24px
- **XL**: 32px
- **XXL**: 48px

### Layout Guidelines
- Use consistent spacing between elements
- Maintain 16px minimum touch targets
- Ensure proper visual hierarchy with spacing
- Use the 8px grid system for alignment

## Responsive Design

### Mobile (320px - 768px)
- Single column layout
- Stacked navigation
- Full-width cards
- Touch-friendly button sizes (minimum 44px)
- Simplified chat interface

### Tablet (768px - 1024px)
- Two-column layout for discussions
- Side-by-side chat and file views
- Larger touch targets
- Optimized for touch interaction

### Desktop (1024px+)
- Multi-column layout
- Sidebar navigation
- Hover states and interactions
- Keyboard navigation support

## Accessibility Standards

### Color Contrast
- **Normal Text**: Minimum 4.5:1 contrast ratio
- **Large Text**: Minimum 3:1 contrast ratio
- **UI Components**: Minimum 3:1 contrast ratio

### Focus Management
- Visible focus indicators on all interactive elements
- Logical tab order
- Skip links for keyboard navigation
- Focus trapping in modals

### Screen Reader Support
- Semantic HTML structure
- ARIA labels for complex components
- Alt text for images
- Descriptive link text

## User Experience Flows

### Primary User Journey

#### 1. Application Entry
```
Landing → Discussion List → Create/Select Discussion
```

#### 2. Discussion Management
```
Discussion List → Create Discussion → Add Files → Start Chat
```

#### 3. File Upload Flow
```
Select Discussion → Drag & Drop Files → Processing → File List
```

#### 4. Chat Interaction
```
Open Chat → Type Question → AI Response → Continue Conversation
```

#### 5. Topic Discovery Flow (NEW)
```
Upload Files → Process Topics → View Topic Directory → Explore by Frequency/File
```

#### 6. Topic Directory Navigation (NEW)
```
Topic Directory → Toggle Group View → Expand File Sections → View Topic Details
```

### Error States and Feedback

#### Success Messages
- **Color**: Accent Magenta (`#C82FFF`)
- **Icon**: `check_circle`
- **Duration**: 3 seconds auto-dismiss

#### Error Messages
- **Color**: Accent Magenta (`#C82FFF`)
- **Icon**: `error`
- **Duration**: Until user action

#### Loading States
- **Spinner**: Material Design circular progress
- **Color**: Accent Magenta (`#C82FFF`)
- **Text**: "Processing..." or specific action

## Component Library Organization

### Atomic Design Structure

#### Atoms
- Button
- Input
- Icon
- Badge
- Spinner

#### Molecules
- Search Bar
- File Upload Area
- Message Bubble
- Discussion Card
- File Item

#### Organisms
- Discussion List
- File Upload Interface
- Chat Interface
- Navigation Header
- **NEW: Topic Directory Interface**
- **NEW: Topic Discovery Pipeline**

#### Templates
- Discussion Page Layout
- Chat Page Layout
- Settings Page Layout
- **NEW: Topic Directory Page Layout**

## Design Tool Integration

### Figma Components
- Create component library in Figma
- Use consistent naming convention
- Include all states and variants
- Document component usage

### Design Tokens
- Export color values as CSS custom properties
- Create spacing scale as design tokens
- Maintain typography scale consistency
- Document animation and transition values

## Animation and Transitions

### Micro-interactions
- **Button Hover**: 0.2s ease-in-out
- **Card Hover**: 0.3s ease-in-out
- **Modal Open**: 0.3s ease-out
- **Loading Spinner**: 1s linear infinite

### Page Transitions
- **Route Changes**: 0.3s ease-in-out
- **Content Loading**: Fade in 0.5s ease-in
- **Error States**: Shake animation 0.5s

## Implementation Guidelines

### CSS Architecture
- Use CSS custom properties for theming
- Implement mobile-first responsive design
- Use BEM methodology for class naming
- Maintain component-scoped styles

### Component Development
- Create reusable, composable components
- Implement proper prop validation
- Include accessibility attributes
- Test across different screen sizes

### Performance Considerations
- Optimize images and assets
- Use efficient CSS selectors
- Implement lazy loading for large lists
- Minimize bundle size

This design system ensures a consistent, accessible, and modern user experience while maintaining the dark theme aesthetic and Material Design principles throughout the Topic-Based Summarizer MVP.
