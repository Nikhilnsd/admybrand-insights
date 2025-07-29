export interface MetricData {
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
