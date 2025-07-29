# Create globals.css with Tailwind and custom styles
globals_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html,
body {
  max-width: 100vw;
  overflow-x: hidden;
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}

a {
  color: inherit;
  text-decoration: none;
}

@media (prefers-color-scheme: dark) {
  html {
    color-scheme: dark;
  }
}

/* Glass effect for cards */
.glass-effect {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}

.dark .glass-effect {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.dark ::-webkit-scrollbar-track {
  background: #1f2937;
}

.dark ::-webkit-scrollbar-thumb {
  background: #4b5563;
}
"""

# Create mockData.ts with realistic sample data
mock_data = """export interface MetricData {
  date: string;
  revenue: number;
  users: number;
  conversions: number;
  campaign: string;
}

export interface CampaignData {
  campaign: string;
  revenue: number;
  users: number;
  conversions: number;
  ctr: number;
  cost: number;
}

// Generate realistic marketing data for the last 30 days
const generateMockData = (): MetricData[] => {
  const data: MetricData[] = [];
  const campaigns = ['Search', 'Social', 'Display', 'Email'];
  const baseDate = new Date();
  baseDate.setDate(baseDate.getDate() - 30);

  for (let i = 0; i < 30; i++) {
    const currentDate = new Date(baseDate);
    currentDate.setDate(baseDate.getDate() + i);
    
    campaigns.forEach(campaign => {
      const users = Math.floor(Math.random() * 500) + 200;
      const conversionRate = Math.random() * 0.15 + 0.05; // 5-20% conversion rate
      const conversions = Math.floor(users * conversionRate);
      const revenuePerConversion = Math.random() * 50 + 25; // $25-75 per conversion
      const revenue = Math.floor(conversions * revenuePerConversion);

      data.push({
        date: currentDate.toISOString().split('T')[0],
        revenue,
        users,
        conversions,
        campaign
      });
    });
  }

  return data;
};

export const mockData: MetricData[] = generateMockData();

// Aggregate campaign performance
export const campaignData: CampaignData[] = [
  'Search', 'Social', 'Display', 'Email'
].map(campaign => {
  const campaignMetrics = mockData.filter(d => d.campaign === campaign);
  const totalRevenue = campaignMetrics.reduce((sum, d) => sum + d.revenue, 0);
  const totalUsers = campaignMetrics.reduce((sum, d) => sum + d.users, 0);
  const totalConversions = campaignMetrics.reduce((sum, d) => sum + d.conversions, 0);
  
  return {
    campaign,
    revenue: totalRevenue,
    users: totalUsers,
    conversions: totalConversions,
    ctr: Math.random() * 5 + 2, // 2-7% CTR
    cost: Math.floor(totalRevenue * (Math.random() * 0.3 + 0.2)) // 20-50% of revenue as cost
  };
});

// Summary metrics
export const summaryMetrics = {
  totalRevenue: mockData.reduce((sum, d) => sum + d.revenue, 0),
  totalUsers: mockData.reduce((sum, d) => sum + d.users, 0),
  totalConversions: mockData.reduce((sum, d) => sum + d.conversions, 0),
  averageOrderValue: mockData.reduce((sum, d) => sum + d.revenue, 0) / mockData.reduce((sum, d) => sum + d.conversions, 0),
  conversionRate: (mockData.reduce((sum, d) => sum + d.conversions, 0) / mockData.reduce((sum, d) => sum + d.users, 0)) * 100
};
"""

# Create utility functions
utils_ts = """import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Format currency
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount);
}

// Format number with commas
export function formatNumber(num: number): string {
  return new Intl.NumberFormat('en-US').format(num);
}

// Format percentage
export function formatPercentage(num: number): string {
  return `${num.toFixed(1)}%`;
}

// Calculate growth percentage
export function calculateGrowth(current: number, previous: number): number {
  if (previous === 0) return 0;
  return ((current - previous) / previous) * 100;
}

// Export to CSV functionality
export function exportToCSV(data: any[], filename: string) {
  const csvContent = convertToCSV(data);
  downloadCSV(csvContent, filename);
}

function convertToCSV(data: any[]): string {
  if (data.length === 0) return '';
  
  const headers = Object.keys(data[0]);
  const csvRows = [
    headers.join(','),
    ...data.map(row => 
      headers.map(header => {
        const value = row[header];
        return typeof value === 'string' ? `"${value}"` : value;
      }).join(',')
    )
  ];
  
  return csvRows.join('\\n');
}

function downloadCSV(csvContent: string, filename: string) {
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  const url = URL.createObjectURL(blob);
  
  link.setAttribute('href', url);
  link.setAttribute('download', filename);
  link.style.visibility = 'hidden';
  
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
"""

# Write the files
with open(f"{project_name}/styles/globals.css", "w") as f:
    f.write(globals_css)

with open(f"{project_name}/data/mockData.ts", "w") as f:
    f.write(mock_data)

with open(f"{project_name}/lib/utils.ts", "w") as f:
    f.write(utils_ts)

print("Created core files:")
print("  - styles/globals.css")
print("  - data/mockData.ts")
print("  - lib/utils.ts")