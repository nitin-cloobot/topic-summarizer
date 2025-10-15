# Frontend - Topic-Based Summarizer

React + Vite application for the Topic-Based Summarizer MVP.

## 🏗️ Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── common/         # Reusable components
│   │   ├── discussion/     # Discussion components
│   │   ├── file/           # File upload components
│   │   └── chat/           # Chat interface
│   ├── pages/              # Main pages
│   │   ├── HomePage/
│   │   ├── DiscussionPage/
│   │   └── NotFoundPage/
│   ├── services/           # API services
│   │   ├── api/            # API client
│   │   └── utils/          # Utilities
│   ├── App.jsx             # Main app component
│   ├── App.css
│   ├── main.jsx            # Entry point
│   └── index.css           # Global styles
├── public/                 # Static assets
├── index.html              # HTML template
├── package.json            # Dependencies
└── vite.config.js          # Vite configuration
```

## 🚀 Setup

1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## 🎨 Design System

### Colors
- **Background**: `#0D0D0D` to `#4D4D4D`
- **Accent**: `#C82FFF` (Magenta), `#00AAFF` (Blue)
- **Text**: `#FFFFFF` (Primary), `#A8A8A8` (Secondary)

### Typography
- **Font Family**: Montserrat
- **Weights**: 400 (Regular), 500 (Medium), 600 (Semi-Bold)
- **Icons**: Material Symbols Outlined (Weight 200)

### Components
- **Button**: Primary (gradient), Secondary (solid), Danger (accent)
- **Modal**: Centered overlay with backdrop
- **Form**: Inputs with rounded corners (4px max)
- **Card**: Elevated surface with border
- **Chat Bubbles**: Capsule shape (16px radius)

### Spacing Scale
- XS: 4px
- S: 8px
- M: 16px
- L: 24px
- XL: 32px
- XXL: 48px

## 📚 Components

### Common Components
- `Button` - Customizable button (primary/secondary/danger)
- `Modal` - Modal dialog
- `LoadingSpinner` - Loading indicator
- `ErrorMessage` - Error display

### Discussion Components
- `DiscussionList` - Grid of discussion cards
- `DiscussionCard` - Single discussion card
- `DiscussionForm` - Create/edit form
- `DiscussionDetail` - Discussion header

### File Components
- `FileUpload` - Drag & drop upload
- `FileList` - List of uploaded files
- `FileStatus` - Upload status messages

### Chat Components
- `ChatInterface` - Main chat container
- `MessageList` - Message history
- `MessageInput` - Input field
- `MessageBubble` - Single message

## 🔌 API Integration

API services in `src/services/api/`:
- `discussions.js` - Discussion CRUD
- `files.js` - File upload
- `chat.js` - Chat messages

## 🛠️ Development

### Adding a New Component

1. Create component folder:
```
src/components/[category]/[ComponentName]/
├── ComponentName.jsx
└── ComponentName.css
```

2. Follow design system guidelines
3. Use CSS custom properties
4. Implement responsive design

### Styling Guidelines

- Use CSS custom properties from `index.css`
- Follow BEM naming convention
- Mobile-first responsive design
- Maintain 8px grid system

### Code Style

- Use functional components with hooks
- PropTypes for prop validation (optional)
- Descriptive variable names
- Keep components focused and small

## 📱 Responsive Breakpoints

- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

## 🧪 Testing

Run tests:
```bash
npm test
```

## 🚀 Build

Production build:
```bash
npm run build
```

Preview build:
```bash
npm run preview
```

## 📦 Dependencies

- **react**: ^18.3.1
- **react-dom**: ^18.3.1
- **react-router-dom**: ^6.26.0
- **vite**: ^5.4.2

## 🎯 Best Practices

1. **Components**: Keep them small and focused
2. **State**: Use hooks appropriately
3. **API**: Handle errors gracefully
4. **Styling**: Follow design system
5. **Performance**: Optimize re-renders
6. **Accessibility**: Use semantic HTML

## 🔍 Debugging

1. Check browser console for errors
2. Use React DevTools
3. Verify API responses in Network tab
4. Check component props and state

