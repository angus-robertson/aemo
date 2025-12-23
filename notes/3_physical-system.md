## Section 3: Understanding how the physical market works

### Generation and dispatch 

#### The spot market provides transparent price signals for real-time dispatch and system balancing
The NEM Dispatch Engine (NEMDE) runs a complex dispatch process, selecting the lowest cost combination of generator and load offers to meet demand across the NEM, subject to technical constraints on the power system. 

The output from NEMDE is a set of regional electricity 'pool' prices and dispatch instructions for generators and loads. Generators are paid the reigonal pool price for the energy they produce, and retailers and other market customers must pay the regional pool price for the energy they consume in the region. AEMO manages the settlement of the market.

The wholesale market is supported by a suite of mechanisms to manage system security and market volatility, including price caps and floors and intervention powers.

**Figure 3a: Key features of the NEM's wholesale spot market**
- Energy only: Generators are paid only for the electricity they produce and sell into the market, with no seperate payments for simply being available. This model relies on scarcity pricing to ensure sufficient investment in generation (e.g. during periods of tight supply, prices can spike up to very high levels and provide a return on capital intensive investment). This approach creates a strong link between actual supply and financial reward, encouraging efficient operation and investment.
- Mandatory, gross pool: Generators (above a certain capacity threshold) are required to bid into the market and be dispatched, but are only paid for the actual electricity they provide and deliver, with spot prices determined by supply and demand at five-minute intervals. The supply curve for electricity depends on which generators are available and what their costs are. Demand is forecast by the market operator and has historically been inelastic in the short-run.
- Real time: Generators are responsible for self-commitment and there is no day-ahead schedule. While AEMO retains residual powers to ensure that the power system balances, it is generators who are primarily responsible for monitoring market information and being ready to meet the power system requirements.
- Uniform clearing price: All generators that are dispatched receive the same market price. The price is set by the highest-priced (marginal) bid required to meet demand in each five-minute interval. This model encourages generators to bid their true marginal cost. This leads to greater market efficiency and transparency. Uniform-clearing also facilitates liquid derivatives markets which are important for managing spot price risks.

#### How does AEMO work out operational demand?

### Ancillary services

#### Ancillary markets serve to procure essential system services to maintain real-time system reliability
The secure and reliable real-time operation of the NEM depends not only on having sufficient generation (managed through the wholesale spot market), but also on a suite of technical capabilities known as ESS.

**Figure 3b: Key ESS**
- Frequency control:
- Inertia:
- System strength:
- Voltage control and reactive power:
- Reserves: 
- System restart services:

Under the NEL, AEMO is responsible for maintaining power system security and ensuring the availiability of ESS in real-time. AEMO directly contract some of these services (such as network support and control ancillary services, NSCAS, and system restart ancillary services, SRAS) and uses markets for others (such as frequency control ancillary services, FCAS). Services including inertia and system strength have only recently begun to attract attention as traditional sources (such as coal-fired plant) retire. Historically, these services were effectively provided as byproducts of large synchronous generators, such as coal, gas and hydro, and did not require explicit procurement or pricing.

Ancillary service costs are recovered from market participants through a regulated cost allocation framework.



### Transmission and distribution

Key features of the NEM's transmission network:
- **open access and cost allocation**: under the NEM's open access regime, any generator may connect to the network provided they meet technical standards and fund their connection infrastructure - they do not pay for ongoing use of the shared transmission system. Instead, these costs are recovered from consumers. This arrangement encourages investment in generation, but does not guarantee generators receive unconstrained access to the market.[^note1] 
- **interconnection and regional pricing**: the NEM is divided into five regions, each with a designated `Regional Reference Node`. Spot prices are calaculated at these nodes and reflect local supply-demand conditions. Interconnectors link the regions, allowing electricity to flow from lower- to higher-priced regions, helping to moderate prices and improve reliability. However, when interconnectors reach capacity, regional prices can separate, potentially leading to sharp price differences for market participants operating across regional boundaries.
- **losses and congestion**: electricity is lost as it travels long distances. These losses are captured through Marginal Loss Factors (MLFs) which adjust a generator's market revenue to reflect the actual value their electricity delivers to the system. MLFs are updated annually and can vary dependeing upon anticipated power flows from new loads and generators. In addition, transmission congestion can occur hwen the physical limits on the network prevent the lowest-cost generation from being dispatched. When this happens, some generators are 'constrained off' and higher-cost local generators may set the market price. 

Centralised, long-term planning is essential to ensure transmission investment occurs in the right places, at the right scale and with sufficient lead  time. 

[^note1]: NSW's Access Scheme diverges from this principle by allocating access rights in Renewable Energy Zones (REZs).