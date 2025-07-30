# ADmyBRAND Insights - Analytics Dashboard

A modern, interactive analytics dashboard built with Next.js 14, TypeScript, Tailwind CSS, and Recharts. This project showcases advanced data visualization, real-time updates, and beautiful UI/UX design for digital marketing agencies.

![Dashboard Preview](https://via.placeholder.com/800x400/3B82F6/FFFFFF?text=ADmyBRAND+Insights+Dashboard)

## 🚀 Features

### 📊 Analytics & Visualization
- **Interactive Charts**: Line, Area, Bar, and Pie charts with hover effects
- **Real-time Data Updates**: Simulated live data refresh every 5 seconds
- **Responsive Design**: Perfect display on desktop, tablet, and mobile devices
- **Data Export**: Export campaign data to CSV format

### 🎨 Modern UI/UX
- **Dark/Light Theme Toggle**: Seamless theme switching with persistent preferences
- **Glassmorphism Effects**: Modern glass-style cards with backdrop blur
- **Smooth Animations**: Framer Motion powered micro-interactions
- **Loading Skeletons**: Elegant loading states for better UX

### 📱 Advanced Features
- **Sortable Data Table**: Click column headers to sort data
- **Advanced Filtering**: Search campaigns, filter by revenue range
- **Pagination**: Handle large datasets efficiently
- **Sidebar Navigation**: Professional dashboard layout

## 🛠️ Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Build Tool**: Webpack (via Next.js)

## 📋 Quick Setup

### Prerequisites
- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. **Extract the ZIP file and navigate to the project directory**
   ```bash
   cd admybrand-insights-fixed
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

### Build for Production

```bash
# Build the application
npm run build

# Start production server
npm run start
```

## 📁 Project Structure

```
admybrand-insights-fixed/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout component
│   └── page.tsx           # Main dashboard page
├── components/            # React components
│   ├── Charts.tsx         # Interactive chart components
│   ├── Dashboard.tsx      # Main dashboard component
│   ├── DataTable.tsx      # Advanced data table
│   ├── LoadingSkeleton.tsx # Loading states
│   ├── MetricCard.tsx     # Metric display cards
│   ├── Sidebar.tsx        # Navigation sidebar
│   └── ThemeToggle.tsx    # Dark/light theme toggle
├── data/                  # Data layer
│   └── mockData.ts        # Sample analytics data
├── lib/                   # Utility functions
│   └── utils.ts           # Helper functions
├── styles/                # Styling
│   └── globals.css        # Global styles and Tailwind
├── package.json           # Dependencies and scripts
├── tailwind.config.js     # Tailwind configuration
├── tsconfig.json          # TypeScript configuration
└── next.config.js         # Next.js configuration
```

## 🎯 Key Components

### MetricCard
Displays key performance indicators with trend indicators and smooth animations.

### Charts
Interactive data visualizations including:
- Revenue trend area chart
- Campaign performance bar chart
- Conversion distribution pie chart
- Multi-metric line chart

### DataTable
Advanced table with:
- Column sorting
- Search functionality
- Revenue range filtering
- CSV export capability
- Pagination

### Dashboard
Main component orchestrating all features with real-time updates and loading states.

## 📊 Sample Data

The dashboard uses realistic sample marketing data including:
- **Daily Metrics**: Revenue, users, conversions across 30 days
- **Campaign Data**: Performance across Search, Social, Display, and Email channels
- **Summary Statistics**: Aggregated KPIs and growth percentages

## 🔧 Customization

### Adding New Charts
Add new chart types in `components/Charts.tsx`:

```tsx
// Example: Add a new chart type
export function NewChart({ data }: { data: any[] }) {
  return (
    <ResponsiveContainer width="100%" height={250}>
      <YourChartType data={data}>
        {/* Chart configuration */}
      </YourChartType>
    </ResponsiveContainer>
  );
}
```

### Modifying Theme Colors
Update colors in `tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      primary: '#your-color',
      secondary: '#your-color',
    }
  }
}
```

### Adding New Metrics
Extend the data structure in `data/mockData.ts`:

```typescript
export interface MetricData {
  // Add new fields here
  newMetric: number;
}
```

## 🚀 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy automatically with each push

### Netlify
1. Build the project: `npm run build`
2. Deploy the `out` directory to Netlify

### Other Platforms
The project is compatible with any static hosting platform that supports Next.js.

## 🎨 Design Philosophy

This dashboard follows modern design principles:
- **Minimalist**: Clean, uncluttered interface
- **Data-First**: Information architecture prioritizes key metrics
- **Responsive**: Mobile-first approach ensuring accessibility
- **Performance**: Optimized for fast loading and smooth interactions

## 🔍 AI Tools Used

This project was developed using various AI-assisted tools:
- **GitHub Copilot**: Code completion and suggestion
- **ChatGPT**: Architecture planning and problem-solving
- **v0.dev**: UI component generation and styling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🌟 Acknowledgments

- Next.js team for the amazing framework
- Tailwind CSS for the utility-first CSS framework
- Recharts for beautiful data visualizations
- Framer Motion for smooth animations

  
## 📄 License

MIT License — use freely, share proudly 🚀

---

> 💡 by Nikhil S Doshikar
