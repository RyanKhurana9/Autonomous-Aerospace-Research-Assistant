from langchain_core.tools import tool
import arxiv
import requests
@tool
def search_arxiv(query: str) -> str:
    """Search aerospace research papers from arXiv."""
    client = arxiv.Client()                          
    search = arxiv.Search(query=query, max_results=3)
    papers = []
    for result in client.results(search):          
        papers.append(f"Title: {result.title}\nSummary: {result.summary}\n")
    return "\n\n".join(papers)

@tool
def get_nasa_data(query: str) -> str:
    """Retrieve NASA technical information."""
    
    url = f"https://images-api.nasa.gov/search?q={query}"
    response = requests.get(url)

    if response.status_code != 200:
        return "NASA API ERROR"

    data = response.json()
    items = data["collection"]["items"][:3]

    if not items:
        return "No NASA results found."

    results = []

    for item in items:
        title = item["data"][0]["title"]
        description = item["data"][0].get("description", "")
        results.append(f"{title}\n{description}")

    return "\n\n".join(results)
@tool
def rocket_exhaust_velocity(Isp: float) -> str:
    """Calculate rocket exhaust velocity using specific impulse."""

    g=9.81
    ve = Isp * g
    return f"Exhaust velocity is approximately {ve} m/s"
@tool 
def search_arxiv(query: str) -> str:
    """Search aerospace and engineering research papers from arXiv.
    Use for finding academic papers on propulsion, aerodynamics, orbital mechanics,
    spacecraft design, atmospheric science, and related topics.
    """
    client = arxiv.Client()#connet to arxiv client
    search = arxiv.Search(query=query, max_results=5, sort_by=arxiv.SortCriterion.Relevance)
    papers = []
    for i in client.results(search):
        papers.append(f"Title:{i.title}\nSUMMARY:{i.summary}\nAUTHOR:{i.authors}\nURL:{i.entry_id}\n")
    if papers==None:
        return "No papers found."
    else:
        return "\n\n".join(papers)
@tool 
def get_nasa_data(query:str)->str:
    """Retrieve NASA techinical information and data.
    use for finding technical information on spacecraft,prpulsion systems, aerodynamics, atmospheric science, and related topics.
    and AEROSPACE ENGINEERING.
    """
    url=f"https://images-api.nasa.gov/search?q={query}"
    response=requests.get(url)
    if response.status_code!=200:#check if the API request was successful
        return "NASA API ERROR"
    data=response.json()
    items=data['collection']['items'][:5]#get the first 5 item from the seatch reults
    if not items:
        return "NO NASA results found"
    result=[]
    for item in items:
        title=item['data'][0]['title']
        description=item['data'][0].get('description','')
        result.append(f"{title}\n{description}")
    return "\n\n".join(result)
@tool
def get_ISS_location()->dict:
    """ Get the current location of the Internationa Space station(ISS)
    use for trackint the current location of the ISS and its trajectory.
    """
    url='http://api.open-notify.org/iss-now.json'
    response=requests.get(url)
    if response.status_code!=200:
        return {"error":"ISS API Error"}
    data=response.json()
    position=data['iss_position']
    return {"latitude":position['latitude'],"longitude":position['longitude']}
@tool
def reynolds_number(density: float, velocity: float, length: float, viscosity: float) -> str:
    """Calculate Reynolds number to determine flow regime (laminar vs turbulent)."""
    Re = (density * velocity * length) / viscosity
    regime = "Laminar" if Re < 5e5 else "Turbulent"
    return f"Reynolds Number: {Re:.2e} — {regime} flow"
@tool 
def calculate_drag_forece(density: float, velocity: float, area: float, drag_coefficient: float) -> str:
    """Calculate aerodynamic drag force on a spacecraft."""
    drag_force = 0.5 * density * velocity**2 * area * drag_coefficient
    return f"Drag Force: {drag_force:.2f} N"
@tool 
def calculate_orbital_period(semi_major_axis: float) -> str:
    """Calculate the orbital period of a satellite using Kepler's third law."""
    G = 6.67430e-11  # Gravitational constant
    M = 5.972e24     # Mass of Earth in kg
    T = 2 * 3.14159 * (semi_major_axis**3 / (G * M))**0.5
    return f"Orbital Period: {T / 3600:.2f} hours"

@tool
def clauclate_propulsion_efficiency(thrust:float,power:float)->float:
    '''CALCUALTE THE PROPULSION EFFICIENCY OF A ROCKET ENGINE'''
    efficiency=(thrust*9.81)/power
    return f"Propulsion Efficiency: {efficiency:.2f}"
@tool
def propellant_mass_flow(thrust_N: float, Isp: float) -> str:
    """Calculate propellant mass flow rate from thrust and specific impulse."""
    g = 9.81
    mdot = thrust_N / (Isp * g)
    return f"Propellant mass flow rate: {mdot:.2f} kg/s"
@tool 
def calculate_mach_Number(velocity:float,speed_of_sound:float)->str:
    """Calculate the Mach number to determine the speed regime of a vehicle."""
    Mach=velocity/speed_of_sound
    return f"Mach Number: {Mach:.2f}"
@tool 
def calcualte_thrust_to_weight_ratio(thrust:float,mass:float)->float:
    """ calculate the thrust to weight ratio of a rocket or spacecraft."""
    return f"Thrust to weight ratio:{thrust/(mass*9.81):.2f}"#.2f means to round the results to 2 decimal places

    

         
         
    

   



     


